from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy import text
from fastapi import Depends

from core.config import app_settings, logging
from models.post import PostModel
from db.db import get_db_session

# from .common import DBObjectService
# from db.es import get_elastic
# from schemas.schemas import SearchSchema
from typing import Any, Generic, Type, TypeVar, List
from db.db import Base
from pydantic import BaseModel

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

    async def create(self, *args, **kwargs):
        pass

    async def update(self, *args, **kwargs):
        pass

    async def delete(self, *args, **kwargs):
        pass
