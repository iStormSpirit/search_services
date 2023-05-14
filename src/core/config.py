import logging
import os
from pydantic import BaseSettings, PostgresDsn

from .logger import LOGGING

logging.basicConfig(**LOGGING)


class AppSettings(BaseSettings):
    database_dsn: PostgresDsn
    project_name: str
    project_description: str
    project_version: str
    project_host: str
    project_port: int
    # es_host: str
    # es_index: str
    # es_resp_size: int

    class Config:
        env_file = '.env'


app_settings = AppSettings()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
