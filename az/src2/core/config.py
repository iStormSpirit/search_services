import logging

from pydantic import BaseSettings, PostgresDsn

from .logger import LOGGING

logging.basicConfig(**LOGGING)


class ApiSettings(BaseSettings):
    database_dsn: PostgresDsn
    el_host: str
    index: str
    resp_size: int

    class Config:
        env_file = '.env'


app_settings = ApiSettings()
