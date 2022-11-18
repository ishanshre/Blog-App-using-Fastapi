from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config():
        orm_mode = True