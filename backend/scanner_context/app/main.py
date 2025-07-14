from fastapi import FastAPI, Depends
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/postgres')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

app = FastAPI(title="ScannerContext")

LISTING_CONTEXT_URL = os.getenv('LISTING_CONTEXT_URL', 'http://listing_context:8000')

class ScanRequest(BaseModel):
    shop_url: str

@app.post('/scan')
def scan(req: ScanRequest):
    resp = requests.get(f'{LISTING_CONTEXT_URL}/listings', params={'shop_url': req.shop_url})
    listings = resp.json()
    # TODO: simulate scraping suspect listings
    violations = []
    for listing in listings:
        violations.append({'original_listing_id': listing['id'], 'suspect_url': 'https://example.com', 'similarity_score': 0.9})
    return {'violations': violations}
