import os
import sys
from pathlib import Path

def check_status():
    print("=" * 50)
    print("PipelineIQ - Project Status Check")
    print("=" * 50)
    print()
    
    issues = []
    warnings = []
    
    # Check Python version
    py_version = sys.version_info
    if py_version >= (3, 11):
        print(f"✓ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    else:
        print(f"✗ Python {py_version.major}.{py_version.minor}.{py_version.micro} (need 3.11+)")
        issues.append("Python version too old")
    
    # Check Node.js
    node_check = os.system("node --version >nul 2>&1")
    if node_check == 0:
        print("✓ Node.js installed")
    else:
        print("✗ Node.js not found")
        issues.append("Node.js not installed")
    
    # Check backend structure
    print("\nBackend:")
    backend_files = [
        "backend/main.py",
        "backend/requirements.txt",
        "backend/.env.example",
        "backend/agents/pipeline_agent.py",
        "backend/utils/docker_sandbox.py",
        "backend/utils/results_writer.py"
    ]
    for file in backend_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file}")
            issues.append(f"Missing {file}")
    
    # Check backend .env
    if Path("backend/.env").exists():
        print("  ✓ backend/.env")
        # Check for required keys
        with open("backend/.env") as f:
            env_content = f.read()
            required = ["OPENAI_API_KEY", "GITHUB_CLIENT_ID", "GITHUB_CLIENT_SECRET", "JWT_SECRET_KEY"]
            for key in required:
                if f"{key}=" in env_content and "your_" not in env_content.split(f"{key}=")[1].split("\n")[0]:
                    print(f"    ✓ {key} configured")
                else:
                    print(f"    ⚠ {key} needs configuration")
                    warnings.append(f"{key} not configured")
    else:
        print("  ✗ backend/.env (run setup.bat)")
        issues.append("Backend .env missing")
    
    # Check frontend structure
    print("\nFrontend:")
    frontend_files = [
        "frontend/package.json",
        "frontend/vite.config.js",
        "frontend/index.html",
        "frontend/src/App.jsx",
        "frontend/src/main.jsx",
        "frontend/src/services/api.js"
    ]
    for file in frontend_files:
        if Path(file).exists():
            print(f"  ✓ {file}")
        else:
            print(f"  ✗ {file}")
            issues.append(f"Missing {file}")
    
    # Check frontend .env
    if Path("frontend/.env").exists():
        print("  ✓ frontend/.env")
    else:
        print("  ✗ frontend/.env (run setup.bat)")
        warnings.append("Frontend .env missing")
    
    # Check dependencies
    print("\nDependencies:")
    if Path("backend/venv").exists() or Path("backend/env").exists():
        print("  ✓ Backend virtual environment")
    else:
        print("  ⚠ Backend virtual environment not found")
        warnings.append("Run: cd backend && python -m venv venv")
    
    if Path("frontend/node_modules").exists():
        print("  ✓ Frontend node_modules")
    else:
        print("  ⚠ Frontend dependencies not installed")
        warnings.append("Run: cd frontend && npm install")
    
    # Summary
    print("\n" + "=" * 50)
    if not issues:
        print("✓ All critical checks passed!")
        if warnings:
            print(f"\n⚠ {len(warnings)} warning(s):")
            for w in warnings:
                print(f"  - {w}")
        print("\nReady to run: start.bat")
    else:
        print(f"✗ {len(issues)} issue(s) found:")
        for i in issues:
            print(f"  - {i}")
        print("\nRun setup.bat first!")
    print("=" * 50)

if __name__ == "__main__":
    check_status()
