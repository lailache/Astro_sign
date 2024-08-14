from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import SqlAlchemyBase


class ZodiacSign(SqlAlchemyBase):
    __tablename__ = 'zodiac_signs'

    sign_id: Mapped[int] = mapped_column(primary_key=True)
    sign_name: Mapped[str] = mapped_column(String(50))
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]

    predictions = relationship("Prediction", back_populates="zodiac_sign")

    def __repr__(self):
        return f'<ZodiacSign {self.sign_id}: "{self.sign_name}">'
