from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    location: str