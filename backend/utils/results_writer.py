import json
import os
from typing import Dict, Optional
from datetime import datetime

class ResultsWriter:
    def __init__(self, results_dir: str = "results"):
        self.results_dir = results_dir
        os.makedirs(results_dir, exist_ok=True)
    
    def write(self, run_id: str, data: Dict) -> str:
        """Write results to JSON file"""
        filepath = os.path.join(self.results_dir, f"{run_id}.json")
        
        # Add metadata
        data["metadata"] = {
            "run_id": run_id,
            "generated_at": datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        return filepath
    
    def read(self, run_id: str) -> Optional[Dict]:
        """Read results from JSON file"""
        filepath = os.path.join(self.results_dir, f"{run_id}.json")
        
        if not os.path.exists(filepath):
            return None
        
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def list_all(self) -> list:
        """List all result files"""
        files = [f for f in os.listdir(self.results_dir) if f.endswith('.json')]
        return sorted(files, reverse=True)
