from datetime import datetime

from sqlalchemy import Date, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import SqlAlchemyBase


class AppUser(SqlAlchemyBase):
    __tablename__ = 'app_users'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(100), default='Mr. Incognito')
    birth_date: Mapped[datetime] = mapped_column(Date)
    birth_time: Mapped[Time] = mapped_column(Time)
    birth_place: Mapped[str] = mapped_column(String(100))

    user_preferences = relationship("UserPreference", back_populates="app_user")

    def __repr__(self):
        return f'<AppUser {self.id}: "{self.name}">'
