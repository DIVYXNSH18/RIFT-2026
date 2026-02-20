@echo off
echo ========================================
echo PipelineIQ - Initial Setup
echo ========================================
echo.

REM Check if backend .env exists
if not exist "backend\.env" (
    echo [1/2] Creating backend/.env from template...
    copy "backend\.env.example" "backend\.env" >nul
    echo     Created! Please edit backend/.env with your credentials.
) else (
    echo [1/2] backend/.env already exists
)

REM Check if frontend .env exists
if not exist "frontend\.env" (
    echo [2/2] Creating frontend/.env...
    echo VITE_API_URL=http://localhost:8000 > "frontend\.env"
    echo     Created!
) else (
    echo [2/2] frontend/.env already exists
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit backend/.env with your credentials:
echo    - OPENAI_API_KEY
echo    - GITHUB_CLIENT_ID
echo    - GITHUB_CLIENT_SECRET
echo    - JWT_SECRET_KEY
echo.
echo 2. Run: start.bat
echo.
pause
