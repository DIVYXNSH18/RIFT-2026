# PipelineIQ - Project Overview

## What is PipelineIQ?

PipelineIQ is a production-ready CI/CD pipeline AI agent that automatically detects, analyzes, and fixes failing tests in your GitHub repositories. It uses a multi-agent architecture powered by LangGraph and GPT-4 to intelligently debug and repair code.

## Key Features

### 🤖 Multi-Agent Architecture
- **7 specialized agents** working in sequence
- **LangGraph orchestration** for complex workflows
- **Configurable retry limits** (default: 5 attempts)
- **Real-time state management**

### 🔒 Security & Sandboxing
- **Docker-based sandboxing** for safe code execution
- **GitHub OAuth authentication**
- **JWT token-based security**
- **Resource limits and capability restrictions**

### 📊 Real Pipeline Analysis
- **No fake data** - analyzes actual test failures
- **Generates results.json** for each run
- **Tracks success/failure metrics**
- **Timeline visualization**

### 🎨 Modern UI
- **React 19** with custom animations
- **Real-time status updates**
- **Score tracking and visualization**
- **Responsive design**

## How It Works

### 1. User Flow
```
User → Login with GitHub → Enter Repo URL → Run Agent → View Results
```

### 2. Agent Workflow
```
Clone Repo → Detect Failures → Analyze Root Cause → 
Generate Fixes → Apply Fixes → Run Tests → Commit Changes
```

### 3. Technical Flow
```
Frontend (React) → API (FastAPI) → Agent (LangGraph) → 
Sandbox (Docker) → Results (JSON)
```

## Architecture

### Backend Stack
- **FastAPI** - Modern Python web framework
- **LangGraph** - Multi-agent orchestration
- **LangChain** - LLM integration
- **OpenAI GPT-4** - Code analysis and generation
- **Docker** - Sandboxed execution
- **Redis** - State management (optional)
- **PyGithub** - GitHub API integration

### Frontend Stack
- **React 19** - UI framework
- **Vite** - Build tool and dev server
- **Custom CSS** - Animations and styling
- **Fetch API** - HTTP client

### Infrastructure
- **GitHub OAuth** - Authentication
- **JWT** - Token-based security
- **Docker Compose** - Container orchestration
- **Environment Variables** - Configuration

## Project Structure

```
RIFT 2026/
├── backend/                    # Python backend
│   ├── agents/
│   │   └── pipeline_agent.py  # Multi-agent system
│   ├── utils/
│   │   ├── docker_sandbox.py  # Sandboxed execution
│   │   └── results_writer.py  # Results management
│   ├── results/               # Generated JSON files
│   ├── main.py                # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   ├── .env.example           # Environment template
│   └── docker-compose.yml     # Docker config
│
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── services/
│   │   │   └── api.js         # API client
│   │   ├── App.jsx            # Main component
│   │   └── main.jsx           # Entry point
│   ├── package.json           # Node dependencies
│   ├── vite.config.js         # Vite config
│   └── .env                   # Frontend config
│
├── setup.bat                   # Initial setup
├── start.bat                   # Launch script
├── status.py                   # Status checker
├── health_check.py             # Health monitor
├── menu.bat                    # Interactive menu
│
├── README.md                   # Setup guide
├── WORKFLOW.md                 # Developer guide
├── TESTING.md                  # Test checklist
└── INTEGRATION.md              # Integration guide
```

## Getting Started

### Quick Start (3 steps)
```bash
# 1. Setup
setup.bat

# 2. Configure backend/.env with your credentials

# 3. Run
start.bat
```

### Detailed Setup
See `README.md` for complete instructions.

## Use Cases

### 1. Automated Test Fixing
- Detects failing tests automatically
- Analyzes root causes using AI
- Generates and applies fixes
- Validates fixes by re-running tests

### 2. CI/CD Pipeline Monitoring
- Monitors GitHub repositories
- Tracks test success rates
- Provides detailed failure analysis
- Generates actionable insights

### 3. Code Quality Improvement
- Identifies code issues
- Suggests improvements
- Applies best practices
- Maintains code standards

## Configuration

### Environment Variables

**Backend (`backend/.env`):**
```env
OPENAI_API_KEY=...              # Required
GITHUB_CLIENT_ID=...            # Required
GITHUB_CLIENT_SECRET=...        # Required
JWT_SECRET_KEY=...              # Required
MAX_RETRY_LIMIT=5               # Optional
DOCKER_SANDBOX_ENABLED=true     # Optional
```

**Frontend (`frontend/.env`):**
```env
VITE_API_URL=http://localhost:8000
```

### Customization

**Retry Limit:**
- Default: 5 attempts
- Configure in `backend/.env`
- Can be overridden per request

**Agent Behavior:**
- Edit `backend/agents/pipeline_agent.py`
- Modify LLM prompts
- Add new agent nodes
- Change state transitions

**UI Styling:**
- Edit `frontend/src/App.css`
- Modify animations
- Update color scheme
- Change layout

## API Endpoints

### Authentication
- `GET /auth/github` - Get OAuth URL
- `GET /auth/github/callback` - Handle callback

### Pipeline
- `POST /api/pipeline/run` - Trigger agent
- `GET /api/pipeline/results/{run_id}` - Get results
- `GET /api/pipeline/status/{run_id}` - Get status

### Documentation
- `GET /docs` - Interactive API docs
- `GET /redoc` - Alternative docs

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

### Integration Tests
See `TESTING.md` for complete checklist.

## Deployment

### Development
```bash
start.bat
```

### Production

**Backend:**
```bash
cd backend
docker-compose up -d
```

**Frontend:**
```bash
cd frontend
npm run build
# Deploy dist/ folder
```

## Monitoring

### Health Checks
```bash
python health_check.py
```

### Status Checks
```bash
python status.py
```

### Logs
- Backend: Console output
- Frontend: Browser console
- Docker: `docker logs <container>`

## Troubleshooting

### Common Issues

**Backend won't start:**
- Check Python version (need 3.11+)
- Verify `.env` file exists
- Check port 8000 availability

**Frontend won't start:**
- Check Node version (need 18+)
- Run `npm install`
- Check port 5173 availability

**OAuth not working:**
- Verify GitHub OAuth app settings
- Check callback URL matches exactly
- Ensure credentials in `.env`

**API calls failing:**
- Check backend is running
- Verify `VITE_API_URL` in frontend
- Check browser console for errors

See `README.md` for detailed troubleshooting.

## Contributing

1. Fork repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## Resources

### Documentation
- `README.md` - Setup guide
- `WORKFLOW.md` - Developer workflow
- `TESTING.md` - Testing guide
- `INTEGRATION.md` - Integration guide

### External Links
- FastAPI: https://fastapi.tiangolo.com/
- LangGraph: https://langchain-ai.github.io/langgraph/
- React: https://react.dev/
- Vite: https://vitejs.dev/

## License

MIT License - Team Jigyasa

## Team

Team Jigyasa - RIFT 2026

## Support

For help:
1. Check documentation files
2. Review API docs at `/docs`
3. Check browser/console logs
4. Verify environment setup

---

**Version:** 1.0.0  
**Last Updated:** 2024  
**Status:** Production Ready ✓
