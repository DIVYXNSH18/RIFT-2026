from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from agents.error_solver_agent import ErrorSolverAgent, ErrorSolverConfig

router = APIRouter(prefix="/api/error-solver", tags=["Error Solver"])

class ErrorSolverRequest(BaseModel):
    errors: List[Dict]
    code_content: str
    language: str

class ErrorSolverResponse(BaseModel):
    solutions: List[Dict]
    total_errors: int
    solved_errors: int

@router.post("/solve", response_model=ErrorSolverResponse)
async def solve_errors(request: ErrorSolverRequest):
    """Solve errors using Gemini AI"""
    try:
        # Initialize error solver with Gemini
        solver = ErrorSolverAgent()
        
        # Solve errors
        solutions = await solver.solve_errors(
            request.errors, 
            request.code_content, 
            request.language
        )
        
        # Count solved errors
        solved_count = sum(1 for sol in solutions if sol.get('solution') is not None)
        
        return ErrorSolverResponse(
            solutions=solutions,
            total_errors=len(request.errors),
            solved_errors=solved_count
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))