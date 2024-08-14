from datetime import datetime

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import SqlAlchemyBase


class Prediction(SqlAlchemyBase):
    __tablename__ = 'predictions'

    prediction_id: Mapped[int] = mapped_column(primary_key=True)
    sign_id: Mapped[int] = mapped_column(Integer, ForeignKey('zodiac_signs.sign_id'))
    prediction_date: Mapped[datetime]
    prediction: Mapped[str]

    zodiac_sign = relationship("ZodiacSign", back_populates="predictions")

    def __repr__(self):
        return f'<Prediction {self.prediction_id}: "{self.prediction}">'
