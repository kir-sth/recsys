from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from app.database import Base


class Forms(Base):
    __tablename__ = 'forms'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    tg_user_id: Mapped[int]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    description: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    city: Mapped[str]
    quad_key: Mapped[int]
    photo_ids: Mapped[list[str]] = mapped_column(JSON)
    preference_id: Mapped[int] = mapped_column(ForeignKey("preferences.id"))
    min_age: Mapped[int]
    max_age: Mapped[int]
    location_radius: Mapped[float]

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    tg_user_id: Mapped[int]
    name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[str]
    description: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
    city: Mapped[str]
    quad_key : Mapped[int]
    photo_ids: Mapped[list[str]] = mapped_column(JSON)

class Groups(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[Optional[str]]

class Likes(Base):
    __tablename__ = 'likes'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id_from: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user_id_to: Mapped[int] = mapped_column(ForeignKey('users.id'))
    is_match: Mapped[bool]

class Preferences(Base):
    __tablename__ = 'preferences'
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    preferred_gender: Mapped[str]
    min_age: Mapped[int]
    max_age: Mapped[int]
    location_radius: Mapped[float]
