import logging

from pydantic import BaseSettings, PostgresDsn

from .logger import LOGGING

logging.basicConfig(**LOGGING)


class AppSettings(BaseSettings):
    # pass
    database_dsn: PostgresDsn
    project_name: str
    project_description: str
    project_version: str
    project_host: str
    project_port: int
    # el_host: str
    # index: str
    # resp_size: int

    class Config:
        env_file = '.env'


app_settings = AppSettings()
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))