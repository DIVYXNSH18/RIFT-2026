# PipelineIQ - Developer Workflow

## First Time Setup

### 1. Clone and Navigate
```bash
cd "RIFT 2026"
```

### 2. Run Initial Setup
```bash
setup.bat
```
This creates `.env` files from templates.

### 3. Configure Credentials

Edit `backend/.env`:
```env
OPENAI_API_KEY=sk-...                    # Get from OpenAI
GITHUB_CLIENT_ID=...                     # From GitHub OAuth App
GITHUB_CLIENT_SECRET=...                 # From GitHub OAuth App
GITHUB_REDIRECT_URI=http://localhost:8000/auth/github/callback
JWT_SECRET_KEY=your-secret-key-here      # Generate random string
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379
MAX_RETRY_LIMIT=5
DOCKER_SANDBOX_ENABLED=true
API_HOST=0.0.0.0
API_PORT=8000
```

### 4. Setup GitHub OAuth App

1. Go to: https://github.com/settings/developers
2. Click "New OAuth App"
3. Fill in:
   - **Application name**: PipelineIQ
   - **Homepage URL**: http://localhost:5173
   - **Authorization callback URL**: http://localhost:8000/auth/github/callback
4. Copy Client ID and Secret to `backend/.env`

### 5. Install Dependencies

**Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd ..
```

**Frontend:**
```bash
cd frontend
npm install
cd ..
```

### 6. Verify Setup
```bash
python status.py
```

## Daily Development

### Start Everything
```bash
start.bat
```

This opens two terminals:
- Terminal 1: Backend (http://localhost:8000)
- Terminal 2: Frontend (http://localhost:5173)

### Check Health
```bash
python health_check.py
```

### Access Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Development Workflow

### 1. Backend Development

**File Structure:**
```
backend/
├── agents/
│   └── pipeline_agent.py    # Multi-agent logic
├── utils/
│   ├── docker_sandbox.py    # Sandboxed execution
│   └── results_writer.py    # Results management
├── results/                 # Generated JSON results
└── main.py                  # FastAPI routes
```

**Run Backend Only:**
```bash
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

**Test Endpoints:**
```bash
# Health check
curl http://localhost:8000/

# Get GitHub auth URL
curl http://localhost:8000/auth/github

# API docs
# Open: http://localhost:8000/docs
```

### 2. Frontend Development

**File Structure:**
```
frontend/
├── src/
│   ├── services/
│   │   └── api.js          # API client
│   ├── App.jsx             # Main component
│   └── main.jsx            # Entry point
└── .env                    # API URL config
```

**Run Frontend Only:**
```bash
cd frontend
npm run dev
```

**Build for Production:**
```bash
cd frontend
npm run build
# Output in: dist/
```

### 3. Testing

**Backend Tests:**
```bash
cd backend
pytest
```

**Frontend Tests:**
```bash
cd frontend
npm test
```

**Integration Test:**
1. Start both services: `start.bat`
2. Open: http://localhost:5173
3. Click "Login with GitHub"
4. Authorize app
5. Fill in repo details
6. Click "Run Agent"
7. Check results in `backend/results/`

## Common Tasks

### Add New API Endpoint

1. Edit `backend/main.py`:
```python
@app.get("/api/new-endpoint")
async def new_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": "Hello"}
```

2. Update `frontend/src/services/api.js`:
```javascript
async newEndpoint() {
  return this.request('/api/new-endpoint');
}
```

### Modify Agent Behavior

Edit `backend/agents/pipeline_agent.py`:
- Add new agent nodes
- Modify LLM prompts
- Change retry logic
- Update state transitions

### Update UI

Edit `frontend/src/App.jsx`:
- Modify page components
- Update styling
- Add new features

## Troubleshooting

### Backend Issues

**Port 8000 in use:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Dependencies error:**
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt --upgrade
```

**OpenAI API error:**
- Check `OPENAI_API_KEY` in `backend/.env`
- Verify API key is valid
- Check account has credits

### Frontend Issues

**Port 5173 in use:**
```bash
# Kill process or change port in vite.config.js
```

**API calls failing:**
- Check `VITE_API_URL` in `frontend/.env`
- Verify backend is running
- Check browser console for CORS errors

**OAuth not working:**
- Verify callback URL matches exactly
- Check GitHub OAuth app settings
- Ensure backend is on correct port

### Docker Issues

**Sandbox not working:**
- Install Docker Desktop
- Start Docker service
- Set `DOCKER_SANDBOX_ENABLED=true` in `.env`

## Production Deployment

### Backend

**Using Docker:**
```bash
cd backend
docker-compose up -d
```

**Environment:**
- Use HTTPS URLs
- Set strong `JWT_SECRET_KEY`
- Configure production database
- Enable rate limiting
- Add monitoring

### Frontend

**Build:**
```bash
cd frontend
npm run build
```

**Deploy:**
- Upload `dist/` folder to hosting
- Configure environment variables
- Set up CDN (optional)

## Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes
git add .
git commit -m "Add new feature"

# Push
git push origin feature/new-feature

# Create pull request on GitHub
```

## Resources

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **LangGraph Docs**: https://langchain-ai.github.io/langgraph/
- **React Docs**: https://react.dev/
- **Vite Docs**: https://vitejs.dev/

## Support

- Check `README.md` for setup guide
- Check `TESTING.md` for test checklist
- Check `INTEGRATION.md` for integration guide
- Review API docs at http://localhost:8000/docs
