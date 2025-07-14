from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from . import models, schemas, fingerprint

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ListingContext")
model = fingerprint.FingerprintModel()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/listings', response_model=schemas.Listing)
def create_listing(payload: schemas.ListingCreate, db: Session = Depends(get_db)):
    image_hash = model.compute_image_hash(payload.image_url or '')
    embedding = model.compute_text_embedding(payload.description or '')
    listing = models.ListingModel(
        shop_url=payload.shop_url,
        title=payload.title,
        description=payload.description,
        image_url=payload.image_url,
        image_hash=image_hash,
        text_embedding=embedding
    )
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing

@app.get('/listings')
def read_listings(shop_url: str, db: Session = Depends(get_db)):
    listings = db.query(models.ListingModel).filter_by(shop_url=shop_url).all()
    return listings
