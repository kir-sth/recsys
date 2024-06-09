from app.database import async_session_maker
from sqlalchemy.future import select

from app.models import Users, Preferences


async def get_user(user_id: int):
    async with async_session_maker() as session:
        query = select(Users).filter(Users.id == user_id)
        result = await session.execute(query)
    return result.scalars().first()

async def get_users( skip: int = 0, limit: int = 10):
    async with async_session_maker() as session:
        query = select(Users).offset(skip).limit(limit)
        result = await session.execute(query)
    return result.scalars().all()

async def create_user(user: Users):
    async with async_session_maker() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user

async def create_preference(preference: Preferences):
    async with async_session_maker() as session:
        session.add(preference)
        await session.commit()
        await session.refresh(preference)
    return preference
