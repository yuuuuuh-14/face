@echo off
setlocal
echo ===================================================
echo   🧪 Running tests for BIOMETRIC_CONTROL_CENTER 🧪
echo ===================================================

echo.
echo 🛡️ [1/2] Running Python Backend Tests (pytest)...
cd backend
call venv\Scripts\activate.bat
set BCC_ENV=testing
pytest tests/
cd ..

echo.
echo 🌐 [2/2] Running Angular Frontend Tests (vitest)...
cd frontend
REM Running vitest as per package.json
cmd /c yarn test --run
cd ..

echo.
echo ✅ All tests completed.
pause
