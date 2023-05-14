from typing import Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import logging
from db.db import Base

logger = logging.getLogger(__name__)
ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class BaseABCServices:

    def get(self, *args, **kwargs):
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError

    def delete(self, *args, **kwargs):
        raise NotImplementedError


class PostService(BaseABCServices, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self._model = model

    async def get_multi(self, db: AsyncSession, *, skip=0, limit=100):
        statement = select(self._model).offset(skip).limit(limit)
        results = await db.execute(statement=statement)
        return results.scalars().all()

    async def get_by_id(self, db: AsyncSession, post_id):
        statement = select(self._model).where(self._model.id == post_id)
        results = await db.execute(statement=statement)
        return results.scalar_one_or_none()

    async def create(self, db: AsyncSession, data: CreateSchemaType):
        obj_in_data = jsonable_encoder(data)
        db_obj = self._model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, *args, **kwargs):
        pass

    async def delete(self, db: AsyncSession, post_id):
        db_obj = await self.get_by_id(db=db, post_id=post_id)
        if not db_obj:
            logger.info(f'not found post with id {post_id}')
            return None
        await db.delete(db_obj)
        await db.commit()
        logger.info(f'deleted post by id {post_id}')
        return db_obj
