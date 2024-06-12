from sqlalchemy import ForeignKey, JSON, String, Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, List

from app.database import Base


class Forms(Base):
    __tablename__ = 'forms'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    tg_user_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    city: Mapped[str] = mapped_column(String(100))
    quad_key: Mapped[int] = mapped_column(Integer)
    photo_ids: Mapped[List[str]] = mapped_column(JSON)
    preference_id: Mapped[int] = mapped_column(ForeignKey("preferences.id"))
    min_age: Mapped[int] = mapped_column(Integer)
    max_age: Mapped[int] = mapped_column(Integer)
    location_radius: Mapped[float] = mapped_column(Float)

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    tg_user_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    city: Mapped[str] = mapped_column(String(100))
    quad_key: Mapped[int] = mapped_column(Integer)
    photo_ids: Mapped[List[str]] = mapped_column(JSON)

class Likes(Base):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id_from: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user_id_to: Mapped[int] = mapped_column(ForeignKey('users.id'))
    is_match: Mapped[bool] = mapped_column(Boolean)

class Preferences(Base):
    __tablename__ = 'preferences'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    preferred_gender: Mapped[str] = mapped_column(String(10))
    min_age: Mapped[int] = mapped_column(Integer)
    max_age: Mapped[int] = mapped_column(Integer)
    location_radius: Mapped[float] = mapped_column(Float)
