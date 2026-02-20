# Testing Checklist

## Pre-Testing Setup

### Backend Setup
- [ ] Python 3.11+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with all required variables
- [ ] OpenAI API key configured
- [ ] GitHub OAuth app created
- [ ] GitHub Client ID and Secret configured

### Frontend Setup
- [ ] Node.js 18+ installed
- [ ] Dependencies installed (`npm install`)
- [ ] `.env` file created with API URL

## Backend Tests

### API Health Check
- [ ] Backend starts without errors
- [ ] Can access http://localhost:8000
- [ ] API docs available at http://localhost:8000/docs
- [ ] Root endpoint returns version info

### Authentication Tests
- [ ] GET /auth/github returns auth URL
- [ ] Auth URL contains correct client_id
- [ ] OAuth callback handles code parameter
- [ ] JWT token is generated and returned
- [ ] Token can be decoded successfully

### Pipeline Tests (Manual)
- [ ] POST /api/pipeline/run requires authentication
- [ ] Returns 401 without token
- [ ] Accepts valid pipeline request
- [ ] Returns run_id
- [ ] Creates results file in results/ directory
- [ ] GET /api/pipeline/results/{run_id} returns data
- [ ] GET /api/pipeline/status/{run_id} returns status

## Frontend Tests

### UI Tests
- [ ] Landing page loads correctly
- [ ] "Proceed to Dashboard" button works
- [ ] Dashboard shows all tabs (Analyze, Results, Score, Timeline)
- [ ] Login button is visible
- [ ] Forms render correctly

### Navigation Tests
- [ ] Can switch between tabs
- [ ] Empty state shows when no results
- [ ] "Go to Analyze" button works from empty state

### Integration Tests
- [ ] Login button triggers GitHub OAuth
- [ ] OAuth redirects to GitHub
- [ ] After auth, redirects back to app
- [ ] Token is stored in localStorage
- [ ] Form accepts input
- [ ] "Run Agent" button is clickable
- [ ] Loading states show during execution
- [ ] Results display after completion

### API Integration Tests
- [ ] Frontend can reach backend API
- [ ] CORS is configured correctly
- [ ] API calls include auth token
- [ ] Error messages display properly
- [ ] Network errors are handled gracefully

## End-to-End Test Flow

### Complete User Journey
1. [ ] Open http://localhost:5173
2. [ ] See landing page with "Monster" title
3. [ ] Click "Proceed to Dashboard"
4. [ ] See dashboard with Analyze tab active
5. [ ] Click "Login with GitHub"
6. [ ] Redirect to GitHub OAuth
7. [ ] Authorize application
8. [ ] Redirect back to dashboard
9. [ ] See "Successfully logged in" message
10. [ ] Fill in repository URL
11. [ ] Fill in team name
12. [ ] Fill in leader name
13. [ ] Click "Run Agent"
14. [ ] See loading animation
15. [ ] See progress steps updating
16. [ ] Automatically switch to Results tab
17. [ ] See results summary card
18. [ ] See fixes table with data
19. [ ] Switch to Score tab
20. [ ] See score breakdown
21. [ ] Switch to Timeline tab
22. [ ] See timeline visualization

## Performance Tests

- [ ] Backend responds within 2 seconds
- [ ] Frontend loads within 3 seconds
- [ ] API calls complete within 5 seconds
- [ ] No memory leaks in browser
- [ ] No console errors

## Security Tests

- [ ] API requires authentication
- [ ] JWT tokens expire correctly
- [ ] Sensitive data not exposed in responses
- [ ] CORS only allows configured origins
- [ ] No credentials in frontend code
- [ ] Environment variables not committed

## Browser Compatibility

- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)

## Known Issues

Document any issues found:

1. Issue: 
   - Description:
   - Steps to reproduce:
   - Expected behavior:
   - Actual behavior:
   - Workaround:

## Test Results Summary

Date: ___________
Tester: ___________

Total Tests: ___
Passed: ___
Failed: ___
Skipped: ___

Overall Status: [ ] PASS [ ] FAIL

Notes:
