from fastapi import APIRouter

from .api import router as router_post

api_router = APIRouter()
api_router.include_router(router_post)
