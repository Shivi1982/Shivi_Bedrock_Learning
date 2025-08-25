# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AWS Bedrock integration project that demonstrates how to interact with AWS Bedrock foundation models using Python and boto3. The project focuses on invoking various models (particularly Amazon Nova models) for text generation and streaming responses.

## Development Environment

### Virtual Environment Setup
The project uses a virtual environment located at `Shivi_Bedrock_test/`:
```bash
# Activate virtual environment
source Shivi_Bedrock_test/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running Code
Individual Python files can be executed directly:
```bash
python src/initial_invoke.py
python prompts/test_prompts.py
```

## Architecture

### Core Components

1. **Configuration Management** (`project/config.py`):
   - Loads AWS credentials from environment variables
   - Expects: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`

2. **Bedrock Integration** (`src/initial_invoke.py`):
   - Main implementation for AWS Bedrock model invocation
   - Contains both standard and streaming response handling
   - Implements `nova_models()` function for simplified model invocation
   - Tests connection by listing available foundation models

### AWS Bedrock Usage Patterns

The codebase demonstrates two primary invocation methods:
- **Standard invocation**: `bedrock.invoke_model()` - returns complete response
- **Streaming invocation**: `bedrock.invoke_model_with_response_stream()` - provides real-time token generation

## Dependencies

Key packages (from `requirements.txt`):
- `boto3==1.34.0` - AWS SDK for Python
- `python-dotenv==1.0.0` - Environment variable management
- Data analysis: `pandas`, `numpy`, `matplotlib`, `seaborn`

## Important Notes

- AWS credentials are currently hardcoded in `src/initial_invoke.py` (lines 15-17) - these should be moved to environment variables for security
- The project uses Amazon Nova models (`amazon.nova-lite-v1:0`) as the default
- When handling streaming responses, look for `contentBlockDelta` in the chunk data structure