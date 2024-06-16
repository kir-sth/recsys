from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate

from app.models import Users
from app.recommendations.dao import get_user, get_users, create_user
from app.recommendations.recsys import recommend_users
from app.recommendations.schemas import UserSchema


router = APIRouter(
    prefix="",
    tags=["recommendations"]
)


@router.get("recommendations/{user_id}", response_model=Page[UserSchema])
async def get_recommendations(user_id: int):
    current_user = await get_user(user_id)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    all_users = await get_users()
    recommended_user_ids = await recommend_users(current_user, all_users)

    recommended_users = [user for user in all_users if user.id in recommended_user_ids]
    return paginate(recommended_users)


@router.get("/users/{user_id}", response_model=UserSchema)
async def get_single_user(user_id: int):
    current_user = await get_user(user_id=user_id)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user


@router.get("/users")
async def get_all_users():
    all_users = await get_users()
    return all_users


@router.post("/user", response_model=UserSchema)
async def create_new_user(user: UserSchema):
    user_model = Users(
        id=user.id,
        tg_user_id=user.tg_user_id,
        name=user.name,
        age=user.age,
        gender=user.gender,
        description=user.description,
        latitude=user.latitude,
        longitude=user.longitude,
        city=user.city,
        quad_key=user.quad_key,
        photo_ids=user.photo_ids,
    )
    created_user = await create_user(user=user_model)
    if created_user is None:
        raise HTTPException(status_code=500, detail="Failed to create user")
    return created_user
