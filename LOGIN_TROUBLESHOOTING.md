# Login Button Not Responding - Troubleshooting Guide

## Issue
Clicking the "Login with GitHub" button shows no response.

## Root Cause
The backend server is not running or not accessible on http://localhost:8001

## Solution

### Quick Fix (Recommended)
1. Run `start.bat` from the project root directory
   - This will start both backend (port 8001) and frontend (port 5173)

### Manual Fix

#### Step 1: Check if backend is running
```bash
# Run this command
check_backend.bat
```

#### Step 2: Start the backend manually
```bash
cd backend
venv\Scripts\activate
python main.py
```

The backend should start on http://localhost:8001

#### Step 3: Verify backend is running
Open http://localhost:8001/health in your browser
You should see:
```json
{
  "status": "healthy",
  "github_client_id": "Ov23liGH0o...",
  "redirect_uri": "http://localhost:8001/auth/github/callback"
}
```

#### Step 4: Test the login button
1. Open http://localhost:5173
2. Click "Login with GitHub"
3. You should be redirected to GitHub OAuth page

## Additional Checks

### Check 1: Verify .env files exist
- `backend/.env` should exist with GitHub credentials
- `frontend/.env` should have `VITE_API_URL=http://localhost:8001`

### Check 2: Check browser console
1. Open browser DevTools (F12)
2. Go to Console tab
3. Click login button
4. Look for error messages

Common errors:
- "Failed to fetch" = Backend not running
- "CORS error" = Backend CORS not configured
- "404" = Wrong API endpoint

### Check 3: Verify GitHub OAuth App settings
1. Go to GitHub Settings > Developer settings > OAuth Apps
2. Check your OAuth app:
   - Homepage URL: http://localhost:5173
   - Callback URL: http://localhost:8001/auth/github/callback

## Still Not Working?

### Option 1: Restart everything
```bash
# Stop all services
taskkill /F /IM python.exe
taskkill /F /IM node.exe

# Start fresh
start.bat
```

### Option 2: Check ports
```bash
# Check if port 8001 is in use
netstat -ano | findstr :8001

# Check if port 5173 is in use
netstat -ano | findstr :5173
```

### Option 3: Check logs
Look at the terminal where backend is running for error messages

## Success Indicators
✅ Backend running on http://localhost:8001
✅ Frontend running on http://localhost:5173
✅ /health endpoint returns healthy status
✅ Login button redirects to GitHub
✅ After GitHub auth, redirected back with token

## Need More Help?
Check the main README.md troubleshooting section
