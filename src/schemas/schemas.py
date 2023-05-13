from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    text: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: UUID
    text: str
    created_date: datetime
    rubrics: list[str]

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass


class PostInDB(PostInDBBase):
    pass
