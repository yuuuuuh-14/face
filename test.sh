#!/bin/bash

echo "==================================================="
echo "  🧪 Running tests for BIOMETRIC_CONTROL_CENTER 🧪  "
echo "==================================================="

# 1. Backend Tests
echo ""
echo "🛡️ [1/2] Running Python Backend Tests (pytest)..."
cd backend
source venv/bin/activate
export BCC_ENV=testing
pytest tests/
cd ..

# 2. Frontend Tests
echo ""
echo "🌐 [2/2] Running Angular Frontend Tests (vitest)..."
cd frontend
# Vitest is used in this project as per package.json
yarn test --run
cd ..

echo ""
echo "✅ All tests completed."
