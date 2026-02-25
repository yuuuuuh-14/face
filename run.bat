@echo off
setlocal
echo ===================================================

set BCC_ENV=%~1
if "%BCC_ENV%"=="" set BCC_ENV=development

echo.
set /p USE_DOCKER="🐳 Do you want to run with Docker? (y/N, Default: N): "
if /i "%USE_DOCKER%"=="y" (
    echo 🏗️ Starting BCC with Docker Compose...
    docker compose up --build
    goto :eof
)

echo 🌐 Environment: %BCC_ENV%

echo.
echo ▶️ [1/2] Booting Python AI Backend (%BCC_ENV%)...
cd backend

if not exist venv\ (
    echo    📦 Virtual environment not found. Creating 'venv'...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo    📦 Installing backend dependencies...
    pip install -r ..\requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Start the Flask app in a new Command Prompt window so it runs in parallel
echo    ✅ Starting Backend (Port: 8001) in a new window...
start "BCC Backend Server" cmd /c "python app.py"
cd ..


timeout /t 3 /nobreak >nul

echo.
echo ▶️ [2/2] Booting Angular Sci-Fi HUD Frontend...
cd frontend

if not exist node_modules\ (
    echo    📦 'node_modules' not found. Installing frontend dependencies...
    cmd /c yarn install
)

echo    🌐 Starting Angular Live Development Server...
if "%BCC_ENV%"=="production" (
    cmd /c yarn start --configuration production
) else (
    cmd /c yarn start --configuration development
)

echo.
echo 🛑 Shutting down frontend...
echo Note: You may need to manually close the Backend window.
pause
