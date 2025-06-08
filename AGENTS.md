# AGENTS.md - AutoGrading Backend System (For OpenAI Codex Agent - May 2025)

## Project Overview
A simplified AI-powered autograding system for handwritten mathematics assignments using local Python scripts. The system processes scanned assignments through OCR, applies mathematical validation, and provides GPT-based grading with detailed feedback via command-line interface.

**Target Agent**: OpenAI Codex Agent (May 2025 release)
**Execution Environment**: Codex sandbox with iterative testing
**Development Approach**: Complete working system with automated testing

## Project Structure
```
autograding-scripts/
├── src/
│   ├── main.py              # Main processing script and CLI
│   ├── ocr_processor.py     # Pix2Text OCR and image processing
│   ├── symbol_corrector.py  # Mathematical symbol correction
│   ├── gpt_formatter.py     # GPT prompt generation and processing
│   ├── pdf_generator.py     # Graded PDF creation with overlays
│   ├── config.py            # Configuration management
│   └── utils.py             # Utility functions and helpers
├── config/
│   ├── rubrics.yaml         # Grading rubric templates
│   ├── settings.yaml        # Processing configuration
│   └── symbol_mappings.yaml # OCR correction rules
├── input/                   # Input assignment scans
├── output/                  # Generated graded PDFs
├── temp/                    # Temporary processing files
├── logs/                    # Processing logs
├── tests/                   # Sample test files
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
├── setup.py                # Package installation
└── README.md               # Setup and usage instructions
```

## Key Technologies
- **Core**: Python 3.11+, argparse for CLI
- **OCR**: Pix2Text (primary), OpenCV, PIL
- **Math Processing**: SymPy, NumPy
- **PDF Generation**: ReportLab
- **AI Integration**: OpenAI GPT-4 (manual copy-paste workflow)
- **Utilities**: python-dotenv, loguru, pathlib

## Core Functionality

### 1. Command-Line Processing Pipeline
- Simple script execution with file path arguments
- Batch processing for multiple assignments
- Interactive mode with step-by-step guidance
- Progress logging and status updates

### 2. OCR and Image Processing
- Pix2Text integration for mathematical formula recognition
- Image preprocessing (deskew, denoise, contrast enhancement)
- Mathematical symbol correction and validation
- Confidence scoring and quality assessment

### 3. GPT Integration Workflow
- Format OCR results into structured prompts
- Generate copy-paste ready text for manual GPT interaction
- Parse and validate GPT JSON responses
- Handle malformed responses with error recovery

### 4. PDF Generation
- Create professional graded PDFs with feedback overlays
- Maintain original scan quality as background
- Display scores, rubric breakdown, and detailed comments
- Organized file naming and output management

## Development Requirements

### Hardware Requirements
- **CPU**: 2+ cores for OCR processing
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space for dependencies
- **OS**: Windows, macOS, or Linux with Python support

### Software Dependencies
- Python 3.11+ with pip package manager
- Virtual environment support (venv)
- Internet connection for package installation and API calls

### Environment Setup
```bash
# Create virtual environment
python -m venv autograding-env
source autograding-env/bin/activate  # Linux/Mac
# or
autograding-env\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Agent Implementation Instructions

### Codex Agent Capabilities to Leverage
- **Parallel Task Execution**: Build multiple modules simultaneously
- **Iterative Testing**: Automatically test each component until it works
- **Code Quality**: Generate clean, well-documented code with proper error handling
- **Integration Testing**: Ensure all modules work together seamlessly
- **Sandbox Environment**: Full testing capabilities in isolated environment

### Primary Implementation Goals
1. **Create complete, working system** - not just code snippets
2. **Include comprehensive error handling** and user-friendly messages
3. **Build modular, testable components** with clear interfaces
4. **Implement robust logging** for debugging and monitoring
5. **Generate thorough documentation** including setup instructions
6. **Test end-to-end workflow** to ensure everything integrates properly

### Codex Agent Development Approach

### Codex Agent Development Approach

#### CRITICAL REQUIREMENT: Manual GPT Workflow Only
**DO NOT implement direct ChatGPT API integration.** The system must use a manual copy-paste workflow where:
1. System generates structured prompts for GPT
2. User manually copies prompt to ChatGPT interface
3. User copies GPT response back to the system
4. System parses and processes the pasted response

This manual approach provides better educational oversight, cost control, and quality assurance.

#### Single Comprehensive Request
Leverage Codex's parallel processing to build the complete system:

```
Create a complete Python autograding system with MANUAL GPT INTEGRATION (no API):

ARCHITECTURE:
- Command-line Python scripts (no Docker/APIs)
- Pix2Text for mathematical OCR processing
- SymPy for mathematical validation
- ReportLab for PDF generation
- MANUAL copy-paste workflow for GPT integration (NO ChatGPT API)

CRITICAL: GPT Integration Requirements:
- Generate formatted prompts for manual copy-paste to ChatGPT
- Display prompts clearly with copy boundaries
- Pause execution waiting for user to paste GPT response
- Parse pasted JSON responses robustly
- Handle malformed responses gracefully
- NO direct API calls to OpenAI/ChatGPT

MODULES TO BUILD:
1. src/main.py - CLI interface with argparse
2. src/ocr_processor.py - Pix2Text integration + preprocessing
3. src/symbol_corrector.py - Mathematical symbol error correction
4. src/gpt_formatter.py - GPT prompt generation + MANUAL response processing
5. src/pdf_generator.py - Graded PDF creation with overlays
6. src/config.py - Configuration management
7. src/utils.py - Utility functions

CONFIGURATION:
- config/rubrics.yaml - Grading rubric templates
- config/settings.yaml - Processing settings
- config/symbol_mappings.yaml - OCR correction rules
- requirements.txt - Python dependencies (NO openai package)
- .env.example - Environment template (NO OPENAI_API_KEY needed)

FEATURES:
- Interactive mode with step-by-step guidance
- Batch processing for multiple assignments with manual GPT steps
- Debug logging with verbose output
- Comprehensive error handling
- Progress indicators and status updates
- User-friendly copy-paste interface for GPT workflow

MANUAL GPT WORKFLOW SPECIFICATIONS:
- Clear prompt boundaries with "=== COPY TO GPT ===" markers
- Formatted prompts ready for direct paste to ChatGPT
- Input prompts for user to paste GPT responses
- JSON response validation and error handling
- Retry mechanisms for malformed responses
- Progress tracking through batch operations

TEST REQUIREMENTS:
- Verify each module imports correctly
- Test CLI argument parsing
- Validate OCR processing pipeline
- Test prompt generation formatting
- Ensure manual workflow is user-friendly
- Test complete end-to-end workflow with mock GPT responses
- Verify PDF generation works correctly

QUALITY STANDARDS:
- Complete docstrings for all functions
- Type hints where appropriate
- Comprehensive error handling with helpful messages
- Structured logging with different levels
- Clean, readable code following Python conventions
- User-friendly prompts and clear instructions
```

#### Expected Manual GPT Workflow Implementation

**Interactive Mode Example:**
```python
def interactive_gpt_workflow(self, ocr_text, rubric_id):
    """Handle manual copy-paste GPT workflow"""
    
    # Generate prompt
    prompt = self.format_prompt(ocr_text, rubric_id)
    
    # Display for copy-paste
    print("\n" + "="*60)
    print("COPY THE FOLLOWING TO CHATGPT:")
    print("="*60)
    print(prompt)
    print("="*60)
    print("\n1. Copy the above text")
    print("2. Paste it into ChatGPT")
    print("3. Copy the complete JSON response")
    print("4. Paste it below when prompted")
    print("\n" + "-"*60)
    
    # Wait for user response
    while True:
        try:
            print("\nPaste GPT response here:")
            response = input("> ")
            
            if not response.strip():
                print("Please paste the GPT response.")
                continue
                
            # Validate and parse response
            parsed = self.parse_gpt_response(response)
            return parsed
            
        except Exception as e:
            print(f"Error parsing response: {e}")
            print("Please check the JSON format and try again.")
            retry = input("Try again? (y/n): ")
            if retry.lower() != 'y':
                return None
```

**Batch Processing with Manual Steps:**
```python
def batch_process_with_manual_gpt(self, assignment_files):
    """Process multiple assignments with manual GPT steps"""
    
    print(f"Processing {len(assignment_files)} assignments...")
    print("Each assignment will require manual GPT interaction.\n")
    
    for i, file_path in enumerate(assignment_files, 1):
        print(f"\n{'='*50}")
        print(f"ASSIGNMENT {i}/{len(assignment_files)}: {file_path}")
        print(f"{'='*50}")
        
        # Process OCR
        ocr_result = self.process_ocr(file_path)
        
        # Manual GPT step
        print(f"\nReady for GPT grading of assignment {i}")
        input("Press Enter when ready to continue...")
        
        gpt_result = self.interactive_gpt_workflow(ocr_result, rubric_id)
        
        if gpt_result:
            # Generate PDF
            pdf_path = self.generate_graded_pdf(file_path, gpt_result)
            print(f"✅ Completed: {pdf_path}")
        else:
            print(f"❌ Skipped: {file_path}")
        
        # Progress indicator
        print(f"\nProgress: {i}/{len(assignment_files)} completed")
```

#### Testing and Validation Requirements

**Codex should automatically test:**
- Module imports and dependencies
- CLI help and argument parsing
- Basic OCR processing with sample data
- Configuration file loading
- GPT prompt generation and formatting
- Manual workflow user interface
- Response parsing with mock GPT data
- PDF generation functionality
- Error handling for common failure cases

**Integration Testing:**
- Complete workflow from image input to PDF output
- Manual GPT workflow with simulated responses
- Batch processing with multiple files
- Interactive mode user experience
- Debug logging functionality
- Malformed response handling

**Manual Workflow Testing:**
- Generate sample prompts for validation
- Test response parsing with various JSON formats
- Verify error handling for invalid responses
- Ensure user-friendly interface for copy-paste operations

#### Expected Codex Deliverables

**Complete Working System Including:**
- All source code files with proper structure
- Configuration files with sensible defaults
- Requirements.txt with exact versions (NO openai package)
- Comprehensive README.md with manual GPT workflow instructions
- Sample test files and usage examples
- Error handling for common issues
- Logging configuration for debugging
- Clear manual GPT workflow implementation

**Quality Assurance:**
- Code that runs without modification
- Proper Python package structure
- Clear documentation and comments
- Robust error handling with helpful messages
- Cross-platform compatibility (Windows/Mac/Linux)
- User-friendly manual GPT interface
- Reliable response parsing and validation

**Manual GPT Workflow Requirements:**
- NO OpenAI API dependencies or imports
- Clear prompt formatting for copy-paste
- Intuitive user interface for GPT responses
- Robust JSON parsing with error recovery
- Progress tracking through manual steps
- Helpful error messages for malformed responses

### Success Criteria for Codex Agent

**Functional Requirements:**
- [ ] System processes sample math assignment images without errors
- [ ] OCR extraction produces readable mathematical text (>60% accuracy)
- [ ] Symbol correction improves OCR output quality
- [ ] GPT prompt generation creates proper rubric-based prompts
- [ ] Manual GPT workflow is intuitive and user-friendly
- [ ] Response parsing handles various JSON formats correctly
- [ ] PDF generation creates professional graded assignments
- [ ] CLI interface provides helpful feedback and guidance
- [ ] Batch processing handles multiple files with manual GPT steps
- [ ] Error messages are clear and actionable

**Manual GPT Workflow Requirements:**
- [ ] Prompts are clearly formatted for copy-paste
- [ ] User interface guides through manual steps
- [ ] Response input is robust and error-tolerant
- [ ] JSON parsing handles malformed responses gracefully
- [ ] Progress indicators work during batch processing
- [ ] NO API dependencies or OpenAI imports
- [ ] Clear instructions for ChatGPT interaction

**Technical Requirements:**
- [ ] All modules import correctly without dependency issues
- [ ] Configuration files load and validate properly
- [ ] Logging system works across all components
- [ ] File I/O operations handle edge cases gracefully
- [ ] Memory usage stays within reasonable bounds
- [ ] Cross-platform compatibility (Windows/Mac/Linux)
- [ ] Requirements.txt excludes API packages

**Documentation Requirements:**
- [ ] README.md provides clear manual workflow instructions
- [ ] Code includes comprehensive docstrings
- [ ] Configuration files have helpful comments
- [ ] Error messages suggest solutions
- [ ] Usage examples demonstrate manual GPT steps

### Codex-Specific Notes for Manual GPT Implementation

**Critical Implementation Points:**
- **Never import openai** or any ChatGPT API libraries
- **Focus on user experience** for manual copy-paste workflow
- **Robust parsing** for various GPT response formats
- **Clear visual boundaries** for copy-paste sections
- **Progress tracking** that works with manual interruptions
- **Error recovery** when users paste malformed responses

**User Experience Priorities:**
- Make the manual workflow feel smooth and intuitive
- Provide clear guidance at each step
- Handle user errors gracefully with helpful suggestions
- Allow easy retry when responses are malformed
- Track progress clearly during batch operations with manual steps
