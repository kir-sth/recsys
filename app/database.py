from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped

from app.config import settings


engine = create_async_engine(url=settings.postgres_url(), echo=True)
async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    created_datetime_utc: Mapped[datetime] # auto computed
    updated_datetime_utc: Mapped[datetime] # auto computed
