from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings


engine = create_async_engine(url=settings.POSTGRES_URL, echo=True)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
