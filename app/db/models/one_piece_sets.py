from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, Date           # keep Date for the column type
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

if TYPE_CHECKING:
    from .one_piece_cards import OPCard

class OPSet(Base):
    __tablename__ = "one_piece_sets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    released_en: Mapped[int] = mapped_column(Integer)
    released_jp: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(128))
    release_date: Mapped[date | None] = mapped_column(Date, nullable=True)

    cards: Mapped[list["OPCard"]] = relationship(
        back_populates="one_piece_sets",
        cascade="all,delete-orphan",
    )
