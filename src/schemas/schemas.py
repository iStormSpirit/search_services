from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PostBase(BaseModel):
    text: str
    rubrics: list[str]


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: UUID
    created_date: datetime

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass
