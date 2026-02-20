import requests
import sys

def check_health():
    print("Checking PipelineIQ services...\n")
    
    # Check backend
    try:
        response = requests.get("http://localhost:8000/", timeout=3)
        if response.status_code == 200:
            print("✓ Backend API: Running")
            print(f"  {response.json()}")
        else:
            print(f"✗ Backend API: Error {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Backend API: Not running (start backend first)")
    except Exception as e:
        print(f"✗ Backend API: {str(e)}")
    
    # Check frontend
    try:
        response = requests.get("http://localhost:5173/", timeout=3)
        if response.status_code == 200:
            print("✓ Frontend: Running")
        else:
            print(f"⚠ Frontend: Status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("✗ Frontend: Not running (start frontend first)")
    except Exception as e:
        print(f"✗ Frontend: {str(e)}")
    
    print("\nIf services are running:")
    print("  Frontend: http://localhost:5173")
    print("  Backend:  http://localhost:8000")
    print("  API Docs: http://localhost:8000/docs")

if __name__ == "__main__":
    check_health()
