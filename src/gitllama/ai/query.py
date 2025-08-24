"""
AI Query Interface for GitLlama
With integrated context tracking for full transparency
"""

import logging
from typing import List, Optional
from dataclasses import dataclass
from .client import OllamaClient
from ..utils.metrics import context_manager
from ..utils.context_tracker import context_tracker
from .parser import ResponseParser
from .context_compressor import ContextCompressor

logger = logging.getLogger(__name__)


@dataclass
class ChoiceResult:
    """Result from a multiple choice query"""
    index: int
    value: str
    confidence: float
    raw: str
    context_compressed: bool = False
    compression_rounds: int = 0


@dataclass 
class OpenResult:
    """Result from an open response query"""
    content: str
    raw: str
    context_compressed: bool = False
    compression_rounds: int = 0


class AIQuery:
    """Simple interface for AI queries with full context tracking"""
    
    def __init__(self, client: OllamaClient, model: str = "gemma3:4b"):
        self.client = client
        self.model = model
        self.parser = ResponseParser()
        self.compressor = ContextCompressor(client, model)
        self._compression_enabled = True
    
    def choice(
        self, 
        question: str,
        options: List[str],
        context: str = "",
        context_name: str = "choice",
        auto_compress: bool = True
    ) -> ChoiceResult:
        """
        Ask AI to pick from options with full context tracking.
        """
        # Track the input variables
        context_tracker.store_variable(
            f"{context_name}_question",
            question,
            "Multiple choice question"
        )
        context_tracker.store_variable(
            f"{context_name}_options",
            options,
            "Available options for selection"
        )
        if context:
            context_tracker.store_variable(
                f"{context_name}_context",
                context,
                "Context provided for decision"
            )
        
        # Handle context compression if needed
        compressed = False
        compression_rounds = 0
        original_context = context
        
        if auto_compress and self._compression_enabled and context:
            context_to_use, was_compressed = self.compressor.auto_compress_for_query(
                context, 
                self._build_choice_prompt(question, options, "")
            )
            
            if was_compressed:
                logger.info(f"🗜️ Context auto-compressed for choice question")
                context = context_to_use
                compressed = True
                result = self.compressor.compress_context(original_context, question, max_rounds=1)
                compression_rounds = result.compression_rounds
                
                # Track the compressed context
                context_tracker.store_variable(
                    f"{context_name}_compressed_context",
                    context,
                    f"Compressed from {len(original_context)} to {len(context)} chars"
                )
        
        # Build prompt
        prompt = self._build_choice_prompt(question, options, context)
        
        # Track the full prompt
        context_tracker.store_prompt(prompt, context, question)
        
        # Make the query
        messages = [{"role": "user", "content": prompt}]
        
        logger.info(f"🎯 Choice: {question[:50]}... ({len(options)} options)")
        if compressed:
            logger.info(f"   (Using compressed context: {compression_rounds} rounds)")
        context_manager.record_ai_call("choice", question[:50])
        
        # Get response
        response = ""
        for chunk in self.client.chat_stream(self.model, messages, context_name=context_name):
            response += chunk
        
        # Track the response
        context_tracker.store_response(response, "choice")
        
        # Parse the choice
        index, confidence = self.parser.parse_choice(response, options)
        
        result = ChoiceResult(
            index=index,
            value=options[index] if index >= 0 else options[0],
            confidence=confidence,
            raw=response.strip(),
            context_compressed=compressed,
            compression_rounds=compression_rounds
        )
        
        # Track the parsed result
        context_tracker.store_variable(
            f"{context_name}_result",
            {"selected": result.value, "confidence": confidence, "index": index},
            "Parsed choice result"
        )
        
        logger.info(f"✅ Selected: {result.value} (confidence: {confidence:.2f})")
        return result
    
    def open(
        self,
        prompt: str,
        context: str = "",
        context_name: str = "open",
        auto_compress: bool = True
    ) -> OpenResult:
        """
        Ask AI for open response with full context tracking.
        """
        # Track the input variables
        context_tracker.store_variable(
            f"{context_name}_prompt",
            prompt,
            "Open-ended prompt"
        )
        if context:
            context_tracker.store_variable(
                f"{context_name}_context",
                context,
                "Context for open response"
            )
        
        # Handle context compression if needed
        compressed = False
        compression_rounds = 0
        original_context = context
        
        if auto_compress and self._compression_enabled and context:
            context_to_use, was_compressed = self.compressor.auto_compress_for_query(
                context, 
                prompt
            )
            
            if was_compressed:
                logger.info(f"🗜️ Context auto-compressed for open question")
                context = context_to_use
                compressed = True
                result = self.compressor.compress_context(original_context, prompt, max_rounds=1)
                compression_rounds = result.compression_rounds
                
                # Track the compressed context
                context_tracker.store_variable(
                    f"{context_name}_compressed_context",
                    context,
                    f"Compressed from {len(original_context)} to {len(context)} chars"
                )
        
        # Build full prompt
        full_prompt = f"{context}\n\n{prompt}" if context else prompt
        
        # Track the full prompt
        context_tracker.store_prompt(full_prompt, context, prompt)
        
        messages = [{"role": "user", "content": full_prompt}]
        
        logger.info(f"📝 Open: {prompt[:50]}...")
        if compressed:
            logger.info(f"   (Using compressed context: {compression_rounds} rounds)")
        context_manager.record_ai_call("open", prompt[:50])
        
        # Get response
        response = ""
        for chunk in self.client.chat_stream(self.model, messages, context_name=context_name):
            response += chunk
        
        # Track the response
        context_tracker.store_response(response, "open")
        
        # Clean the response
        content = self.parser.clean_text(response)
        
        # Track the cleaned content
        context_tracker.store_variable(
            f"{context_name}_cleaned_response",
            content,
            "Cleaned response content"
        )
        
        result = OpenResult(
            content=content,
            raw=response.strip(),
            context_compressed=compressed,
            compression_rounds=compression_rounds
        )
        
        logger.info(f"✅ Response: {len(content)} chars")
        return result
    
    def _build_choice_prompt(self, question: str, options: List[str], context: str) -> str:
        """Build a simple choice prompt"""
        parts = []
        
        if context:
            parts.append(f"Context: {context}\n")
        
        parts.append(question)
        parts.append("\nOptions:")
        
        for i, option in enumerate(options):
            parts.append(f"{i+1}. {option}")
        
        parts.append("\nRespond with ONLY the number (1, 2, 3, etc) of your choice:")
        
        return "\n".join(parts)
    
    def set_compression_enabled(self, enabled: bool):
        """Enable or disable automatic context compression."""
        self._compression_enabled = enabled
        logger.info(f"Context compression {'enabled' if enabled else 'disabled'}")