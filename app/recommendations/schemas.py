from pydantic import BaseModel
from typing import List, Optional

class UserSchema(BaseModel):
    id: int
    tg_user_id: int
    name: str
    age: int
    gender: str
    description: Optional[str]
    latitude: float
    longitude: float
    city: str
    quad_key: int
    photo_ids: List[str]

    class Config:
        from_attributes = True
