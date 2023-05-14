import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import base
from core.config import app_settings

app = FastAPI(
    title=app_settings.project_name,
    description=app_settings.project_description,
    version=app_settings.project_version,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(base.api_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=app_settings.project_host,
        port=app_settings.project_port,
    )
