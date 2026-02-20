import sys
import os
import subprocess

def check_python():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 11:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    print(f"✗ Python {version.major}.{version.minor}.{version.micro} (need 3.11+)")
    return False

def check_node():
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        version = result.stdout.strip()
        print(f"✓ Node.js {version}")
        return True
    except:
        print("✗ Node.js not found")
        return False

def check_backend_env():
    if os.path.exists('backend/.env'):
        print("✓ Backend .env exists")
        return True
    print("✗ Backend .env missing")
    return False

def check_frontend_env():
    if os.path.exists('frontend/.env'):
        print("✓ Frontend .env exists")
        return True
    print("✗ Frontend .env missing")
    return False

def check_backend_deps():
    if os.path.exists('backend/venv'):
        print("✓ Backend venv exists")
        return True
    print("✗ Backend venv missing")
    return False

def check_frontend_deps():
    if os.path.exists('frontend/node_modules'):
        print("✓ Frontend node_modules exists")
        return True
    print("✗ Frontend node_modules missing")
    return False

def main():
    print("=" * 50)
    print("PipelineIQ - Environment Check")
    print("=" * 50)
    print()
    
    checks = [
        ("Python Version", check_python),
        ("Node.js", check_node),
        ("Backend Config", check_backend_env),
        ("Frontend Config", check_frontend_env),
        ("Backend Dependencies", check_backend_deps),
        ("Frontend Dependencies", check_frontend_deps),
    ]
    
    results = []
    for name, check in checks:
        print(f"Checking {name}...", end=" ")
        result = check()
        results.append(result)
        print()
    
    print()
    print("=" * 50)
    passed = sum(results)
    total = len(results)
    print(f"Results: {passed}/{total} checks passed")
    print("=" * 50)
    
    if passed == total:
        print("\n✓ All checks passed! Ready to start.")
        print("\nRun: start.bat (Windows) or ./start.sh (Linux/Mac)")
    else:
        print("\n✗ Some checks failed. Please fix the issues above.")
        print("\nSetup instructions:")
        print("1. Install Python 3.11+")
        print("2. Install Node.js 18+")
        print("3. Copy backend/.env.example to backend/.env")
        print("4. Create frontend/.env with VITE_API_URL=http://localhost:8000")
        print("5. Run: cd backend && python -m venv venv && pip install -r requirements.txt")
        print("6. Run: cd frontend && npm install")

if __name__ == "__main__":
    main()
