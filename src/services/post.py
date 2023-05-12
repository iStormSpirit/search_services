from elasticsearch import AsyncElasticsearch
from fastapi import Depends
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import app_settings, logging
from db.common import DBObjectService
from db.db import get_db_session
from db.es import get_elastic
from models.post import PostModel
from schemas.schemas import SearchSchema

logger = logging.getLogger(__name__)


class PostService(DBObjectService):
    async def _find_posts_ids(self, query: str) -> list[str]:
        body = SearchSchema(query=query)
        resp = await self.es_session.search(
            index=app_settings.index,
            body=body.search_query,
            size=app_settings.resp_size,
        )
        ids = [p['_source']['id'] for p in resp['hits']['hits']]
        return ids

    async def search_posts(self, query: str) -> list[PostModel]:
        ids = await self._find_posts_ids(query)
        result = await self.db_session.execute(
            select(PostModel).where(PostModel.id.in_(ids)).order_by(PostModel.created_date.desc())
        )
        return result.all()

    async def delete_post(self, post_id: str) -> bool:
        try:
            await self.db_session.execute(
                delete(PostModel).where(PostModel.id == post_id)
            )
            await self.es_session.delete_by_query(
                index=app_settings.index,
                body={'query': {'match': {'id': post_id}}}
            )
            await self.db_session.commit()
        except Exception as ex:
            logger.error(ex)
            return False
        return True


def get_post_service(
        db_session: AsyncSession = Depends(get_db_session),
        es_session: AsyncElasticsearch = Depends(get_elastic)
) -> PostService:
    return PostService(db_session, es_session)
