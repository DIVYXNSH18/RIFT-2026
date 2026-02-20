# Error Solver Agent - Dual AI Integration

## Overview
The Error Solver Agent uses both Google Gemini AI and OpenAI GPT-4 to solve various types of errors:
- Syntax errors
- Logic errors  
- Import errors
- Indentation errors
- Type errors

## Dual AI Strategy
1. **Primary**: Gemini AI attempts to solve the error
2. **Fallback**: OpenAI GPT-4 if Gemini fails
3. **Final Fallback**: Built-in logic for common patterns

## API Endpoint

### Solve Errors
```
POST /api/error-solver/solve
```

**Request:**
```json
{
  "errors": [
    {
      "file": "main.py",
      "line": 10,
      "error": "SyntaxError: invalid syntax",
      "bugType": "SYNTAX",
      "severity": "HIGH"
    }
  ],
  "code_content": "def hello():\n    print('Hello World'\n",
  "language": "python"
}
```

**Response:**
```json
{
  "solutions": [
    {
      "error": {...},
      "solution": {
        "type": "code_replacement",
        "fixed_code": "def hello():\n    print('Hello World')\n",
        "description": "Added missing closing parenthesis"
      },
      "ai_used": "gemini",
      "confidence": 0.9
    }
  ],
  "total_errors": 1,
  "solved_errors": 1
}
```

## Usage Example

```python
import httpx

# Solve errors using dual AI
response = httpx.post("http://localhost:8000/api/error-solver/solve", json={
    "errors": [
        {
            "file": "main.py",
            "line": 1,
            "error": "SyntaxError: invalid syntax",
            "bugType": "SYNTAX",
            "severity": "HIGH"
        }
    ],
    "code_content": "def hello():\n    print('Hello World'\n",
    "language": "python"
})

result = response.json()
for solution in result['solutions']:
    print(f"AI Used: {solution['ai_used']}")
    print(f"Confidence: {solution['confidence']}")
    print(f"Fix: {solution['solution']['description']}")
```

## AI Models Used

- **Gemini Pro**: Primary AI for error solving
- **GPT-4**: Fallback AI when Gemini fails
- **Built-in Logic**: Final fallback for common patterns

## Solution Types

- **code_replacement**: Complete fixed code
- **install_dependency**: Command to install missing packages
- **manual_review**: Cases requiring human intervention

## Response Fields

- `ai_used`: Which AI was used ("gemini", "openai", "builtin")
- `confidence`: Confidence score (0.6-0.9)
- `solution`: The actual fix provided
- `error`: Original error information