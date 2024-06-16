from app.database import async_session_maker
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
import logging

from app.models import Users


logger = logging.getLogger(__name__)


async def get_user(user_id: int):
    try:
        async with async_session_maker() as session:
            query = select(Users).filter(Users.id == user_id)
            result = await session.execute(query)
            return result.scalars().first()
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return None


async def get_users(skip: int = 0, limit: int = 10):
    try:
        async with async_session_maker() as session:
            query = select(Users).offset(skip).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return []


async def create_user(user: Users):
    try:
        async with async_session_maker() as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        return None
