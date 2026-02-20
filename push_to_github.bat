@echo off
echo ========================================
echo Git Push Script - RIFT 2026
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/6] Initializing Git repository...
git init

echo [2/6] Adding all files...
git add .

echo [3/6] Creating commit...
git commit -m "Initial commit - RIFT 2026 Monster CI/CD Agent"

echo [4/6] Setting main branch...
git branch -M main

echo.
echo ========================================
echo MANUAL STEP REQUIRED
echo ========================================
echo.
echo 1. Go to: https://github.com/new
echo 2. Create a new repository named: RIFT-2026
echo 3. Copy the repository URL
echo 4. Enter it below
echo.
set /p REPO_URL="Enter your GitHub repository URL: "

echo.
echo [5/6] Adding remote origin...
git remote add origin %REPO_URL%

echo [6/6] Pushing to GitHub...
echo.
echo You will be prompted for GitHub credentials...
git push -u origin main

echo.
echo ========================================
echo Done!
echo ========================================
echo.
echo Your code is now on GitHub!
echo Repository: %REPO_URL%
echo.
pause
