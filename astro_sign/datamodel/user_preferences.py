from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .model_base import SqlAlchemyBase


class UserPreference(SqlAlchemyBase):
    __tablename__ = 'user_preferences'

    user_id: Mapped[int] = mapped_column(ForeignKey('app_users.user_id'), primary_key=True)
    language: Mapped[str] = mapped_column(String(50))
    theme: Mapped[str] = mapped_column(String(50))

    app_user = relationship("AppUser", back_populates="user_preferences")

    def __repr__(self):
        return f'<UserPreference {self.id}: "{self.language}">'
