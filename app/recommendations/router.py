from fastapi import APIRouter, HTTPException
from fastapi_pagination import paginate

from app.recommendations.dao import get_user, get_users, create_user
from app.recommendations.recsys import recommend_users
from app.recommendations.schemas import UserSchema
from app.models import Users

router = APIRouter(
    prefix="",
    tags=["recommendations"]
)

@router.get("/{user_id}")
async def get_recommendations(user_id: int):
    current_user = await get_user(user_id)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    all_users = await get_users()
    recommended_user_ids = await recommend_users(current_user, all_users)
    
    recommended_users = [user for user in all_users if user.id in recommended_user_ids]
    return paginate(recommended_users)

@router.get("/user/{user_id}")
async def get_single_user(user_id: int):
    current_user = await get_user(user_id=user_id)
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")
    return current_user

@router.get("/users")
async def get_all_users():
    all_users = await get_users()
    return all_users

@router.post("/user")
async def create_new_user(user: UserSchema):
    user_model = Users(
        id=user.id,
        name=user.name,
        age=user.age,
        gender=user.gender,
        location=user.location
    )
    await create_user(user=user_model)
    return {"message": "successful creation"}
