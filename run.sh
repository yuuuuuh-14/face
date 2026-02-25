#!/bin/bash

echo "==================================================="
echo "  🚀 Starting BIOMETRIC_CONTROL_CENTER (BCC) 🚀  "
echo "==================================================="

# Function to handle cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down BCC..."
    if [ -n "$BACKEND_PID" ]; then
        echo "Killing Backend Process (PID: $BACKEND_PID)..."
        kill $BACKEND_PID
    fi
    exit 0
}

# Trap SIGINT and SIGTERM to run cleanup
trap cleanup SIGINT SIGTERM

echo ""
read -p "🐳 Do you want to run with Docker? (y/N): " USE_DOCKER
USE_DOCKER=${USE_DOCKER:-n}

if [[ "$USE_DOCKER" =~ ^[Yy]$ ]]; then
    echo "🏗️  Starting BCC with Docker Compose..."
    docker compose up --build
    exit 0
fi

# Environment Selection (default: development)
export BCC_ENV=${1:-development}
echo "🌐 Environment: $BCC_ENV"

# 1. Start Backend in the background
echo ""
echo "▶️ [1/2] Booting Python AI Backend ($BCC_ENV)..."
cd backend

# Auto-setup venv if not exists
if [ ! -d "venv" ]; then
    echo "   📦 Virtual environment not found. Creating 'venv'..."
    python3 -m venv venv
    source venv/bin/activate
    echo "   📦 Installing backend dependencies..."
    pip install -r ../requirements.txt
else
    source venv/bin/activate
fi

# Run the Flask app in the background
python app.py &
BACKEND_PID=$!
echo "   ✅ Backend is running (PID: $BACKEND_PID, Port: 8001)"
cd ..

# Wait a couple of seconds for backend to initialize
sleep 2

# 2. Start Frontend in the foreground
echo ""
echo "▶️ [2/2] Booting Angular Sci-Fi HUD Frontend..."
cd frontend

# Auto-setup node_modules if not exists
if [ ! -d "node_modules" ]; then
    echo "   📦 'node_modules' not found. Installing frontend dependencies..."
    yarn install
fi

echo "   🌐 Starting Angular Live Development Server..."
if [ "$BCC_ENV" = "production" ]; then
    yarn start --configuration production
else
    yarn start --configuration development
fi

# If frontend exits normally, cleanup backend
cleanup
