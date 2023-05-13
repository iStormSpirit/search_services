from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_db_session
from schemas import schemas as post_schema
from services.base import post_crud
router = APIRouter()



@router.get("/all_posts")
async def read_all_posts(db: AsyncSession = Depends(get_db_session)) -> Any:
    posts = await post_crud.get_multi(db=db)
    return posts


@router.get("/{id}", response_model=post_schema.Post)
async def read_post(*, db: AsyncSession = Depends(get_db_session), post_id) -> Any:
    post = await post_crud.get_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return post


# @router.post("/", response_model=post_schema.Post, status_code=status.HTTP_201_CREATED)
# async def create_post(db: AsyncSession = Depends(get_db_session), ) -> Any:
#     post = {}
#     return post


# @router.put("/{id}", response_model=post_schema.Post)
# async def update_post(*, db: AsyncSession = Depends(get_db_session), id: int) -> Any:
#     post = {}
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
#     return post


# @router.delete("/{id}")
# async def delete_post(*, db: AsyncSession = Depends(get_db_session), id: int) -> Any:
#     post = {}
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
#     return post
