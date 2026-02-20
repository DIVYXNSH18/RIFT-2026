npm run dev
# PipelineIQ Backend

Production-level CI/CD Pipeline AI Agent with multi-agent architecture using LangGraph.

## Features

- ✅ Multi-agent architecture using LangGraph
- ✅ Docker sandboxed code execution
- ✅ GitHub OAuth authentication
- ✅ Configurable retry limit (default: 5)
- ✅ Generates results.json for each run
- ✅ REST API endpoints
- ✅ Real CI/CD pipeline analysis (no fake data)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `GITHUB_CLIENT_ID`: GitHub OAuth App Client ID
- `GITHUB_CLIENT_SECRET`: GitHub OAuth App Client Secret
- `JWT_SECRET_KEY`: Secret key for JWT tokens

### 3. Setup GitHub OAuth App

1. Go to GitHub Settings > Developer settings > OAuth Apps
2. Create a new OAuth App
3. Set Authorization callback URL to: `http://localhost:8000/auth/github/callback`
4. Copy Client ID and Client Secret to `.env`

### 4. Start with Docker Compose

```bash
docker-compose up -d
```

Or run locally:

```bash
uvicorn main:app --reload
```

## API Endpoints

### Authentication

**GET /auth/github**
- Returns GitHub OAuth URL for login

**GET /auth/github/callback?code={code}**
- Handles OAuth callback
- Returns JWT access token

### Pipeline Operations

**POST /api/pipeline/run**
```json
{
  "repo_url": "https://github.com/user/repo",
  "team_name": "TeamName",
  "leader_name": "LeaderName",
  "retry_limit": 5
}
```
- Triggers pipeline agent
- Requires authentication
- Returns run_id and status

**GET /api/pipeline/results/{run_id}**
- Get complete results for a run
- Returns results.json content

**GET /api/pipeline/status/{run_id}**
- Get current status of a run

## Architecture

### Multi-Agent System (LangGraph)

1. **Clone Repo Agent**: Clones repository and creates fix branch
2. **Detect Failures Agent**: Runs tests and detects failures
3. **Analyze Failures Agent**: Uses LLM to analyze root causes
4. **Generate Fixes Agent**: Uses LLM to generate code fixes
5. **Apply Fixes Agent**: Applies fixes to codebase
6. **Run Tests Agent**: Validates fixes
7. **Commit Changes Agent**: Commits and pushes fixes

### Docker Sandbox

- Isolated execution environment
- Resource limits (512MB RAM, 50% CPU)
- No network access for untrusted code
- Security hardened (no-new-privileges, dropped capabilities)

### Results Storage

Each run generates a `results/{run_id}.json` file containing:
- Run metadata
- Repository information
- Detected failures
- Applied fixes
- Commit history
- Timeline of iterations
- Final status

## Usage Example

```python
import httpx

# 1. Login with GitHub
auth_response = httpx.get("http://localhost:8000/auth/github")
# Follow auth_url and get token from callback

# 2. Run pipeline
headers = {"Authorization": f"Bearer {access_token}"}
response = httpx.post(
    "http://localhost:8000/api/pipeline/run",
    json={
        "repo_url": "https://github.com/user/repo",
        "team_name": "MyTeam",
        "leader_name": "John",
        "retry_limit": 5
    },
    headers=headers
)

run_id = response.json()["run_id"]

# 3. Get results
results = httpx.get(
    f"http://localhost:8000/api/pipeline/results/{run_id}",
    headers=headers
)
```

## Security

- JWT-based authentication
- GitHub OAuth for user verification
- Docker sandbox for code execution
- No direct shell access
- Resource limits enforced
- Security-hardened containers

## Production Deployment

1. Use HTTPS in production
2. Set strong JWT_SECRET_KEY
3. Configure proper CORS origins
4. Use production-grade database for results
5. Implement rate limiting
6. Add monitoring and logging
7. Use container orchestration (Kubernetes)

## License

MIT
