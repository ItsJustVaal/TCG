from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from .one_piece_sets import OPSet

class OPCard(Base):
    __tablename__ = "one_piece_cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    set_id: Mapped[int] = mapped_column(ForeignKey("one_piece_sets.id", ondelete="CASCADE"), index=True)
    language: Mapped[str] = mapped_column(String(8), index=True)
    code: Mapped[str] = mapped_column(String(64), index=True)
    name: Mapped[str] = mapped_column(String(256))
    rarity: Mapped[str | None] = mapped_column(String(32), nullable=True)
    color: Mapped[str | None] = mapped_column(String(32), nullable=True)
    wep_type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    type: Mapped[str | None] = mapped_column(String(64), nullable=True)
    power: Mapped[str | None] = mapped_column(String(32), nullable=True)
    cost: Mapped[str | None] = mapped_column(String(32), nullable=True)
    text: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    image_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    set: Mapped["OPSet"] = relationship(back_populates="one_piece_cards")