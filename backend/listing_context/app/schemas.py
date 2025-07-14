from pydantic import BaseModel, Field
from typing import List
from uuid import UUID
from datetime import datetime

class ListingCreate(BaseModel):
    shop_url: str
    title: str
    description: str | None = None
    image_url: str | None = None

class Listing(ListingCreate):
    id: UUID
    image_hash: str | None = None
    text_embedding: List[float] | None = None
    created_at: datetime

    class Config:
        orm_mode = True

class Violation(BaseModel):
    id: UUID
    original_listing_id: UUID
    suspect_url: str
    suspect_image_url: str | None
    similarity_score: float
    platform: str
    reported: bool
    created_at: datetime

    class Config:
        orm_mode = True
