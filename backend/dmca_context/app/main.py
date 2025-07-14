from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

LISTING_CONTEXT_URL = os.getenv('LISTING_CONTEXT_URL', 'http://listing_context:8000')

app = FastAPI(title="DMCAContext")

class GenerateRequest(BaseModel):
    violation_id: str

@app.post('/generate')
def generate(req: GenerateRequest):
    # Placeholder DMCA generation
    notice = f"DMCA notice for violation {req.violation_id}"
    return {"notice": notice}
