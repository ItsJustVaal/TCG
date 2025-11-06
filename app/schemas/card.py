from pydantic import BaseModel

class CardOut(BaseModel):
    id: int
    set_id: int
    game: str
    language: str
    code: str
    name: str
    rarity: str | None = None
    color: str | None = None
    type: str | None = None
    power: str | None = None
    cost: str | None = None
    text: str | None = None
    image_url: str | None = None

    class Config:
        from_attributes = True  # SQLAlchemy -> Pydantic v2
