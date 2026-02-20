import httpx
import asyncio

async def test_backend():
    try:
        # Test health endpoint
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:8001/health")
            print(f"Health check: {response.status_code}")
            print(f"Response: {response.json()}")
            
            # Test GitHub OAuth endpoint
            response = await client.get("http://localhost:8001/auth/github")
            print(f"GitHub OAuth: {response.status_code}")
            print(f"Response: {response.json()}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_backend())