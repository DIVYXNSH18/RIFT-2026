@echo off
echo Checking if backend is running...
curl -s http://localhost:8001/health >nul 2>&1
if %errorlevel% equ 0 (
    echo Backend is running!
    curl http://localhost:8001/health
) else (
    echo Backend is NOT running!
    echo.
    echo To start the backend:
    echo 1. Open a new terminal
    echo 2. cd backend
    echo 3. venv\Scripts\activate
    echo 4. python main.py
    echo.
    echo Or run: start_backend.bat
)
pause
