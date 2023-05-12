from elasticsearch import AsyncElasticsearch
from sqlalchemy.ext.asyncio import AsyncSession


class DBObjectService:

    def __init__(self, db_session: AsyncSession, es_session: AsyncElasticsearch):
        self.db_session = db_session
        self.es_session = es_session
