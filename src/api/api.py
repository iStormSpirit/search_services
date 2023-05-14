from typing import Any, List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_db_session
from schemas import schemas as post_schema
from services.base import post_crud

router = APIRouter()


@router.get("/posts", response_model=List[post_schema.Post])
async def get_all_posts(db: AsyncSession = Depends(get_db_session)) -> Any:
    posts = await post_crud.get_multi(db=db)
    return posts


@router.get("/post/{id}", response_model=post_schema.Post)
async def get_post_by_id(*, db: AsyncSession = Depends(get_db_session), post_id: UUID) -> Any:
    post = await post_crud.get_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return post


@router.post("/post/create/", response_model=post_schema.Post, status_code=status.HTTP_201_CREATED)
async def create_post(*, db: AsyncSession = Depends(get_db_session), data: post_schema.PostCreate) -> Any:
    post = await post_crud.create(db, data)
    return post


@router.delete("/post/{id}/delete")
async def delete_post(*, db: AsyncSession = Depends(get_db_session), post_id: UUID) -> Any:
    post = await post_crud.delete(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return post
