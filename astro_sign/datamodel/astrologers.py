from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .model_base import SqlAlchemyBase


class Astrologer(SqlAlchemyBase):
    __tablename__ = 'astrologers'

    astrologer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    experience_years: Mapped[int]
    rating: Mapped[float]

    def __repr__(self):
        return f'<Astrologer {self.astrologer_id}: "{self.name}">'
