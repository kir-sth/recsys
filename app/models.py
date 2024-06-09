from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    location: Mapped[str]

class Preferences(Base):
    __tablename__ = 'preferences'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    preferred_gender: Mapped[str]
    min_age: Mapped[int]
    max_age: Mapped[int]
    location_radius: Mapped[float]

    user = relationship("Users", back_populates="preferences")

Users.preferences = relationship("Preferences", back_populates="user", uselist=False)
