# GitLlama 🦙🤖

An AI-powered Software Factory that understands your codebase and iteratively builds features. GitLlama v0.6.0 combines deep project analysis with intelligent automation to clone, analyze, create, validate, and deliver production-ready code changes.

## 🌟 Software Factory Features

- **🏭 Production Pipeline**: Complete end-to-end software delivery from analysis to deployment
- **🧠 Deep Project Analysis**: Hierarchical summarization system that understands entire codebases
- **🎯 Deterministic AI Decisions**: Single-word decision system with fuzzy matching for reliability
- **🌿 Intelligent Branch Strategy**: Analyzes existing branches and decides optimal development approach
- **📝 Requirements Integration**: Detects and follows project owner guidance from TODO.md files
- **🔄 Iterative Development**: AI selects and validates files one by one with retry logic and quality gates
- **🎨 Clean Code Generation**: Extracts production-ready code from AI responses, removes thinking noise
- **⚠️ Quality Assurance**: Double-checking validation system with comprehensive error prevention
- **📊 Process Analytics**: Complete tracking of decisions, iterations, and delivery metrics
- **🔄 Interactive Workflow**: AI asks strategic questions for optimal feature understanding
- **📈 Continuous Improvement**: Provides actionable recommendations and development priorities
- **📝 Full Audit Trail**: Complete visibility into every AI decision with context and reasoning

## 🚀 Installation

```bash
pip install gitllama
```

## 📋 Prerequisites

GitLlama requires Ollama for AI-powered features:

```bash
# Install Ollama (if not already installed)
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama server
ollama serve

# Pull a recommended model
ollama pull gemma3:4b
```

## 💻 Usage

### Basic usage (recommended):

```bash
gitllama https://github.com/user/repo.git
```

### With custom model:

```bash
gitllama https://github.com/user/repo.git --model llama3:8b
```

### With specific branch (AI handles all other decisions):

```bash
gitllama https://github.com/user/repo.git --branch feature/my-improvement
```

### Verbose mode (see all AI decisions):

```bash
gitllama https://github.com/user/repo.git --verbose
```

## 🔬 How It Works

GitLlama uses a sophisticated multi-step process to understand and improve repositories:

### 1. **Deep Repository Analysis** 🔍
   - **Step 1: Data Gathering** - Scans all text files, configs, and documentation
   - **Step 2: Smart Chunking** - Groups files to maximize AI context window usage
   - **Step 3: Parallel Analysis** - Each chunk analyzed independently for scalability
   - **Step 4: Hierarchical Merging** - Combines summaries using merge-sort approach
   - **Step 5: Result Formatting** - Creates structured insights about the project

### 2. **Software Factory Pipeline** 🏭
   1. **Repository Acquisition** - Clones and prepares the development environment
   2. **Deep Analysis Phase** - AI explores project structure, patterns, and requirements
   3. **Branch Strategy Planning** - Evaluates existing branches and determines optimal approach
   4. **Development Planning** - AI decides on feature implementation strategy
   5. **Iterative Development** - One-by-one file creation with validation and quality gates
   6. **Quality Assurance** - Automated validation, testing, and error prevention
   7. **Delivery Preparation** - Generates commit messages and prepares for deployment
   8. **Production Deployment** - Pushes verified changes to remote repository

### 3. **Iterative Development Process** 🔄

GitLlama employs a sophisticated iterative development methodology:

```
Starting iterative file modification workflow
============================================================
ITERATION 1: File Selection & Modification
  🤖 AI: Selecting most impactful file for modification
    Selected: src/config.py (CREATE)
    Reason: Add missing configuration management
  📝 AI: Generating optimized content
    ✅ Parsed: 45 lines of clean Python code
    🧹 Trimmed: Removed thinking blocks and extra commentary
  ✅ Validation: File created successfully
  🔍 AI: Double-checking for potential issues
    Status: APPROVED - No warnings detected

ITERATION 2: File Selection & Modification  
  🤖 AI: Selecting next file for enhancement
    Selected: tests/test_config.py (CREATE)
    Reason: Add comprehensive test coverage
  📝 AI: Generating test suite
    ✅ Parsed: 67 lines of clean test code
  ✅ Validation: Tests created and passing
  
AI Decision: Continue with more files? NO (satisfied with changes)
============================================================
Total iterations: 2 | Files modified: 2 | Success rate: 100%
```

#### Development Methodology:
- **🎯 Focused Iteration**: AI selects the most impactful file for each development cycle
- **🔍 Quality Gates**: Each change is validated against project standards before proceeding
- **⚠️ Error Prevention**: Multi-layer validation system eliminates common development issues
- **🎨 Production-Ready Output**: Extracts clean, deployable code from AI responses
- **🔄 Resilient Development**: Up to 3 attempts per file with adaptive goal refinement
- **📊 Process Intelligence**: Comprehensive tracking of development progress and quality metrics

### Example Analysis Output:
```
Starting hierarchical repository analysis
============================================================
STEP 1: DATA GATHERING
  Found 45 files with 12500 total tokens
STEP 2: CHUNKING
  Created 5 chunks for analysis
    Chunk 1: 12 files, 2500 tokens
    Chunk 2: 10 files, 2800 tokens
    Chunk 3: 8 files, 2200 tokens
    Chunk 4: 9 files, 2600 tokens
    Chunk 5: 6 files, 2400 tokens
STEP 3: CHUNK ANALYSIS
  Analyzing 5 chunks
    Processing chunk 1/5...
    Processing chunk 2/5...
    ...
STEP 4: HIERARCHICAL MERGING
  Starting hierarchical merge of 5 summaries
    Level 1: Merging 5 summaries (1800 tokens)
STEP 5: FORMAT RESULTS
  Formatting final results
============================================================
Repository analysis complete!
```

### 4. **Intelligent Branch Selection** 🌿

GitLlama now features sophisticated branch analysis and selection:

```
Starting intelligent branch selection process
============================================================
STEP 1: ANALYZE EXISTING BRANCHES
  Analyzing purposes of 3 branches
    Branch 'feature/auth-system': Production-ready authentication system
    Branch 'wip-database': Work-in-progress database optimization
    Branch 'docs/api': API documentation updates
STEP 2: EVALUATE REUSE POTENTIAL
  Evaluating reuse potential for existing branches
    wip-database: score=45, reasons=work-in-progress branch, matching project type
    feature/auth-system: score=35, reasons=feature branch, matching technologies
STEP 3: MAKE BRANCH DECISION
  Making branch selection decision
🤖 AI: Deciding branch selection strategy with 2 candidates
    Decision: REUSE - High compatibility with existing WIP branch
STEP 4: GENERATE/SELECT BRANCH NAME
  Finalizing branch selection
    Selected existing branch: wip-database
============================================================
Branch selection complete: wip-database
```

#### Branch Selection Features:
- **🔍 Multi-branch Analysis**: Examines all branches in the repository
- **🎯 Smart Scoring**: Evaluates compatibility based on project type, technologies, and purpose
- **🔄 Reuse Preference**: Strongly favors reusing existing branches (80% bias)
- **🏗️ Branch Classification**: Identifies feature, fix, docs, and WIP branches
- **⚙️ Intelligent Fallback**: Creates new branches with meaningful names when needed

### 5. **Production Analytics & Reporting** 📊

GitLlama provides enterprise-grade reporting and process analytics:

#### Analytics Capabilities:
- **🏷️ Version Control**: Complete traceability of software factory versions and configurations
- **⏱️ Process Timeline**: Comprehensive audit trail of all development decisions and actions
- **🔄 Development Cycles**: Detailed analysis of iteration efficiency and success patterns
- **📈 Performance Metrics**: Resource utilization, API efficiency, and processing statistics
- **🎨 Visual Dashboards**: Interactive HTML reports with syntax highlighting and drill-down capabilities
- **🧹 Quality Metrics**: Code cleanliness tracking and output refinement statistics

#### Production Reports:
- **Development Decision Log**: Complete record of AI choices with business context
- **Change Management**: Comprehensive tracking of all file operations and modifications
- **Quality Assurance**: Success rates, retry analysis, and validation effectiveness
- **Strategy Analysis**: Branch selection rationale and development approach optimization
- **Technical Intelligence**: Deep project insights, architecture recommendations, and improvement opportunities

## 🐍 Python API

```python
from gitllama import GitAutomator, AICoordinator

# Software Factory - Full intelligent automation
factory = AICoordinator(model="gemma3:4b")
with GitAutomator(ai_coordinator=factory) as automator:
    results = automator.run_full_workflow(
        git_url="https://github.com/user/repo.git"
    )
    
    print(f"Success: {results['success']}")
    print(f"Branch created: {results['branch']}")
    print(f"Files modified: {results['modified_files']}")
    
    # Access detailed AI analysis
    if 'ai_analysis' in results:
        analysis = results['ai_analysis']
        print(f"Project Type: {analysis['project_type']}")
        print(f"Technologies: {', '.join(analysis['technologies'])}")
        print(f"Code Quality: {analysis['quality']}")
        print(f"Architecture: {analysis['architecture']}")

# Without AI - Simple automation
with GitAutomator() as automator:
    results = automator.run_full_workflow(
        git_url="https://github.com/user/repo.git",
        branch_name="my-branch",
        commit_message="My changes"
    )
```

## 🏗️ Architecture

GitLlama is built with a modular architecture for easy extension:

```
gitllama/
├── cli.py                 # Command-line interface
├── git_operations.py      # Git automation logic
├── ai_coordinator.py      # AI workflow coordination
├── project_analyzer.py    # Hierarchical project analysis
├── branch_analyzer.py     # Intelligent branch selection
├── file_modifier.py       # Iterative development process
├── ai_output_parser.py    # Production-ready code extraction
├── report_generator.py    # Enterprise analytics and reporting
├── context_manager.py     # Performance and resource tracking
├── config.py              # Configuration and logging setup
└── ollama_client.py       # Ollama API integration
```

### Key Components:

- **ProjectAnalyzer**: Handles the 5-step hierarchical analysis process
- **BranchAnalyzer**: Intelligent branch selection with 4-step decision pipeline
- **FileModifier**: Iterative development process with quality gates and resilient retry logic
- **AIOutputParser**: Production-ready code extraction from AI responses with noise elimination
- **ReportGenerator**: Enterprise analytics platform with comprehensive decision tracking and metrics
- **ContextManager**: Performance monitoring and resource optimization for AI operations
- **AICoordinator**: Orchestrates AI decisions throughout the workflow
- **GitAutomator**: Manages git operations with optional AI integration
- **OllamaClient**: Interfaces with local Ollama models

## 🤖 AI Models

The tool works with any Ollama model. Recommended models:

- `gemma3:4b` - Fast and efficient (default)
- `llama3.2:1b` - Ultra-fast for simple tasks
- `codellama:7b` - Optimized for code understanding
- `mistral:7b` - Good general purpose
- `gemma2:2b` - Very fast, good for simple tasks

### Context Window Sizes:
- Small models (1-3B): ~2-4K tokens
- Medium models (7B): ~4-8K tokens
- Large models (13B+): ~8-16K tokens

## 🎯 What Gets Analyzed

GitLlama intelligently analyzes:
- Source code files (Python, JavaScript, Java, Go, Rust, etc.)
- Configuration files (JSON, YAML, TOML, etc.)
- Documentation (Markdown, README, LICENSE)
- Build files (Dockerfile, Makefile, package.json)
- Scripts (Shell, Batch, PowerShell)
- Web assets (HTML, CSS, XML)

## 📊 Analysis Results

The AI provides multi-level insights:

```json
{
  "project_type": "web-application",
  "technologies": ["Python", "FastAPI", "PostgreSQL", "React"],
  "state": "Production-ready with comprehensive test coverage",
  "architecture": "Microservices with REST API",
  "quality": "High - follows best practices",
  "patterns": ["MVC", "Repository Pattern", "Dependency Injection"],
  "analysis_metadata": {
    "total_files": 156,
    "total_tokens": 45000,
    "chunks_created": 12,
    "context_window": 4096,
    "model": "gemma3:4b"
  }
}
```

## ⚙️ Configuration

```bash
# Use a different Ollama server
gitllama https://github.com/user/repo.git --ollama-url http://remote-server:11434

# Use a specific model with more context
gitllama https://github.com/user/repo.git --model codellama:7b

# Verbose output for debugging
gitllama https://github.com/user/repo.git --verbose
```

## 🔧 Extending GitLlama

The modular design makes it easy to add new analysis steps:

```python
# In project_analyzer.py, each step is clearly separated:

def _step1_gather_repository_data(self, repo_path):
    """STEP 1: Gather all repository data"""
    # Add git history analysis here
    # Add dependency scanning here
    # Add security checks here

def _step2_create_chunks(self, files):
    """STEP 2: Create smart chunks"""
    # Add semantic grouping here
    # Add priority-based chunking here

def _step3_analyze_chunks(self, chunks):
    """STEP 3: Analyze each chunk"""
    # Add code quality metrics here
    # Add security scanning here
    # Add performance analysis here
```

## 📈 Performance

- **Small repos (<100 files)**: ~30 seconds
- **Medium repos (100-500 files)**: ~1-2 minutes
- **Large repos (500+ files)**: ~2-5 minutes

*Times vary based on model size and system performance*

## 🛠️ Development

```bash
git clone https://github.com/your-org/gitllama.git
cd gitllama
pip install -e ".[dev]"

# Run tests
pytest

# Check code quality
make lint
make format
make type-check
```

## 🐛 Troubleshooting

### Ollama not available?
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama
ollama serve
```

### Context window too small?
```bash
# Use a model with larger context
gitllama repo.git --model mistral:7b
```

### Analysis taking too long?
```bash
# Use a smaller, faster model
gitllama repo.git --model llama3.2:1b
```

## 📝 License

GPL v3 - see LICENSE file

## 🤝 Contributing

Contributions are welcome! The modular architecture makes it easy to add:
- New analysis steps
- Additional AI models support
- More file type handlers
- Enhanced decision strategies

## 🚀 Core Production Capabilities

- [x] **Iterative Development Process**: Systematic file-by-file development with quality validation
- [x] **Production Code Generation**: Clean, deployable code extraction with noise elimination
- [x] **Quality Assurance Pipeline**: Multi-layer validation system with error prevention
- [x] **Enterprise Analytics**: Complete process tracking, decision auditing, and performance monitoring
- [x] **Resource Optimization**: Intelligent context window management and API efficiency

## 🚀 Future Factory Enhancements

- [ ] **Historical Analysis**: Git commit pattern analysis and developer workflow optimization
- [ ] **Security Pipeline**: Dependency vulnerability scanning and security-first development
- [ ] **Parallel Processing**: Multi-threaded chunk analysis for enterprise-scale repositories
- [ ] **Quality Metrics**: Comprehensive code quality scoring and improvement recommendations
- [ ] **Security Integration**: Built-in security analysis and compliance validation
- [ ] **Test Automation**: Intelligent test coverage assessment and generation
- [ ] **Pull Request Automation**: AI-generated PR descriptions and review facilitation
- [ ] **Documentation Factory**: Multi-language documentation generation and maintenance
- [ ] **Team Collaboration**: Real-time collaborative development and workflow coordination

---

**Enterprise Note**: GitLlama Software Factory requires git credentials configured for repository deployment. Ensure proper access rights and compliance with your organization's development policies before production use.