# Frontend-Backend Integration Guide

## Quick Setup

### 1. Update Login Button in Navbar

Replace the Login button onClick handler in `App.jsx`:

```javascript
import api from './services/api';

// In Navbar component, replace the Login button:
<button
  onClick={async () => {
    const { auth_url } = await api.getGithubAuthUrl();
    window.location.href = auth_url;
  }}
  // ... rest of button props
>
  Login with GitHub
</button>
```

### 2. Update handleRun function

Replace the handleRun function in App component:

```javascript
import api from './services/api';

const handleRun = useCallback(async () => {
  setIsLoading(true);
  setLoadingStep(0);
  
  try {
    // Call real API
    const response = await api.runPipeline(
      formData.repoUrl,
      formData.teamName,
      formData.leaderName
    );
    
    // Simulate loading steps
    for (let step = 0; step < 4; step++) {
      setLoadingStep(step);
      await new Promise(resolve => setTimeout(resolve, 900));
    }
    
    // Get results
    const results = await api.getResults(response.run_id);
    
    setIsLoading(false);
    setHasResults(true);
    setActivePage("results");
    
    // Store results in state
    setCurrentResults(results);
    
  } catch (error) {
    console.error('Pipeline run failed:', error);
    alert('Failed to run pipeline: ' + error.message);
    setIsLoading(false);
  }
}, [formData]);
```

### 3. Add state for current results

Add this to App component state:

```javascript
const [currentResults, setCurrentResults] = useState(null);
```

### 4. Use real results in pages

Update renderPage to use currentResults:

```javascript
case "results":
  return <ResultsPage results={currentResults || mockResults} />;
```

### 5. Handle GitHub OAuth Callback

Add this useEffect in App component:

```javascript
useEffect(() => {
  // Check for OAuth callback
  const params = new URLSearchParams(window.location.search);
  const code = params.get('code');
  
  if (code) {
    api.handleGithubCallback(code).then(() => {
      // Remove code from URL
      window.history.replaceState({}, document.title, window.location.pathname);
      alert('Successfully logged in!');
    }).catch(err => {
      console.error('Login failed:', err);
    });
  }
}, []);
```

## Testing

1. Start backend: `cd backend && docker-compose up`
2. Start frontend: `cd frontend && npm run dev`
3. Open http://localhost:5173
4. Click "Login with GitHub"
5. After auth, fill form and click "Run Agent"

## Environment Variables

Frontend `.env`:
```
VITE_API_URL=http://localhost:8000
```

Backend `.env`:
```
OPENAI_API_KEY=your_key
GITHUB_CLIENT_ID=your_id
GITHUB_CLIENT_SECRET=your_secret
JWT_SECRET_KEY=your_secret
```
