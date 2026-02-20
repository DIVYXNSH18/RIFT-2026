import docker
import asyncio
from typing import Optional

class DockerSandbox:
    def __init__(self):
        self.client = docker.from_env()
        self.container: Optional[docker.models.containers.Container] = None
        
    async def start(self):
        """Start a sandboxed container"""
        self.container = self.client.containers.run(
            "python:3.11-slim",
            command="sleep infinity",
            detach=True,
            network_mode="bridge",
            mem_limit="512m",
            cpu_quota=50000,
            security_opt=["no-new-privileges:true"],
            cap_drop=["ALL"],
            volumes={
                "/tmp/workspace": {"bind": "/workspace", "mode": "rw"}
            }
        )
        
        # Install git and other tools
        await self.execute_command("apt-get update && apt-get install -y git curl")
        
    async def execute_command(self, command: str, timeout: int = 300) -> str:
        """Execute command in sandbox"""
        if not self.container:
            await self.start()
        
        try:
            exec_result = self.container.exec_run(
                f"/bin/bash -c '{command}'",
                demux=True,
                stream=False
            )
            
            stdout = exec_result.output[0].decode() if exec_result.output[0] else ""
            stderr = exec_result.output[1].decode() if exec_result.output[1] else ""
            
            return stdout + stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    async def cleanup(self):
        """Stop and remove container"""
        if self.container:
            self.container.stop()
            self.container.remove()
            self.container = None
    
    def __del__(self):
        """Cleanup on deletion"""
        if self.container:
            try:
                self.container.stop()
                self.container.remove()
            except:
                pass
