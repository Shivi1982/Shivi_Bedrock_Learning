#!/bin/bash

echo "🚀 Activating AWS Bedrock Project Environment..."

# Activate virtual environment
source Shivi_Bedrock_test/bin/activate

# Load environment variables
export $(grep -v '^#' .env | xargs)

echo "✅ Virtual environment activated"
echo "✅ Environment variables loaded"
echo ""
echo "To test AWS Bedrock connection, run:"
echo "  python src/initial_invoke.py"
echo ""
echo "To deactivate when done, type: deactivate"