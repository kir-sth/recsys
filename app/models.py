from sqlalchemy import Column, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, Float, Boolean
from app.database import Base

class Forms(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    tg_user_id = Column(Integer)
    group_id = Column(Integer, ForeignKey("groups.id"))
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    quad_key = Column(Integer)
    photo_ids = Column(JSON)
    preference_id = Column(Integer, ForeignKey("preferences.id"))
    preference = relationship("Preferences", back_populates="forms")
    min_age = Column(Integer)
    max_age = Column(Integer)
    location_radius = Column(Float)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    tg_user_id = Column(Integer)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String)
    quad_key = Column(Integer)
    photo_ids = Column(JSON)

class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    user_id_from = Column(Integer, ForeignKey('users.id'))
    user_id_to = Column(Integer, ForeignKey('users.id'))
    is_match = Column(Boolean)

class Preferences(Base):
    __tablename__ = 'preferences'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    preferred_gender = Column(String)
    min_age = Column(Integer)
    max_age = Column(Integer)
    location_radius = Column(Float)
    forms = relationship("Forms", back_populates="preference")
