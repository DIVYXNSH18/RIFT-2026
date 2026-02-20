@echo off
cls
echo.
echo ========================================
echo   PipelineIQ - Monster CI/CD AI Agent
echo ========================================
echo.
echo Project Structure:
echo   backend/     - FastAPI + LangGraph multi-agent system
echo   frontend/    - React 19 + Vite UI
echo.
echo Quick Commands:
echo   setup.bat           - First time setup (create .env files)
echo   python status.py    - Check project status
echo   start.bat           - Run everything
echo   python health_check.py - Check if services are running
echo.
echo Documentation:
echo   README.md       - Complete setup guide
echo   WORKFLOW.md     - Developer workflow
echo   TESTING.md      - Testing checklist
echo   INTEGRATION.md  - Integration guide
echo.
echo URLs (when running):
echo   Frontend:  http://localhost:5173
echo   Backend:   http://localhost:8000
echo   API Docs:  http://localhost:8000/docs
echo.
echo ========================================
echo.
echo What would you like to do?
echo.
echo [1] First time setup (create .env files)
echo [2] Check project status
echo [3] Start application
echo [4] Check health
echo [5] Exit
echo.
set /p choice="Enter choice (1-5): "

if "%choice%"=="1" (
    call setup.bat
) else if "%choice%"=="2" (
    python status.py
    pause
) else if "%choice%"=="3" (
    call start.bat
) else if "%choice%"=="4" (
    python health_check.py
    pause
) else if "%choice%"=="5" (
    exit
) else (
    echo Invalid choice
    pause
    call %0
)
