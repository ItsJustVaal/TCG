# from fastapi import APIRouter, Depends, Query
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from app.api.deps import get_db
# from app.db.models import HLSet, HLCard
# from app.schemas.card import CardOut

# router = APIRouter(prefix="/cards", tags=["cards"])

# @router.get("", response_model=list[CardOut])
# async def list_cards(
#     db: AsyncSession = Depends(get_db),
#     game: str | None = Query(None),
#     set_code: str | None = Query(None),
#     rarity: str | None = Query(None),
#     color: str | None = Query(None),
#     limit: int = Query(50, ge=1, le=200),
#     offset: int = Query(0, ge=0),
# ):
#     stmt = select(Card).limit(limit).offset(offset)
#     if game:
#         stmt = stmt.where(Card.game == game)
#     if rarity:
#         stmt = stmt.where(Card.rarity == rarity)
#     if color:
#         stmt = stmt.where(Card.color == color)
#     if set_code:
#         # join-free filter if you also store set code on card (optional). If not, join Set.
#         stmt = stmt.where(Card.code.like(f"{set_code}-%"))
#     res = await db.execute(stmt)
#     return res.scalars().all()

# @router.get("/{code}", response_model=CardOut)
# async def get_card(code: str, db: AsyncSession = Depends(get_db)):
#     stmt = select(Card).where(Card.code == code)
#     res = await db.execute(stmt)
#     obj = res.scalar_one_or_none()
#     if not obj:
#         from fastapi import HTTPException
#         raise HTTPException(status_code=404, detail="Card not found")
#     return obj
