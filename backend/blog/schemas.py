from pydantic import BaseModel
from typing import Optional

class PostBase(BaseModel):
    title: str
    body: str


class PostCreate(BaseModel):
    is_published: Optional[bool]
    pass

class Post(PostBase):
    id: int
    author_id: int

    
    class Config():
        orm_mode = True