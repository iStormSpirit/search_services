from datetime import datetime

from pydantic import BaseModel, validator
from config.logger import logging

logger = logging.getLogger(__name__)


class PostModelBase(BaseModel):
    id: str | None
    text: str


class PostModelFull(PostModelBase):
    created_date: datetime
    rubrics: list

    @validator('text', pre=True)
    def convert_text(cls, value) -> str:
        value = value[0].strip('"')
        if isinstance(value, str):
            return value
        try:
            return str(value)
        except Exception as ex:
            logger.error(f'text convert error: {ex}')

    @validator('created_date', pre=True)
    def convert_date(cls, value) -> datetime:
        value = value[1].strip('()')
        if isinstance(value, datetime):
            return value
        try:
            datetime_obj = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            return datetime_obj
        except Exception as ex:
            logger.error(f'datetime_obj error: {ex}')

    @validator('rubrics', pre=True)
    def convert_rubrics(cls, value) -> list:
        value = value[2].strip('"')
        if isinstance(value, list):
            return value
        try:
            value_clr = value[1:-1].split(', ')
            rubrics_lst = [elem[1:-1] for elem in value_clr]
            return rubrics_lst
        except Exception as ex:
            logger.error(f'rubrics error: {ex}')

    @staticmethod
    def parse_csv_to_dict(value) -> dict:
        text = PostModelFull.convert_text(value)
        date = PostModelFull.convert_date(value)
        rubrics = PostModelFull.convert_rubrics(value)
        result_dict = {'text': text, 'created_date': date, 'rubrics': rubrics}
        return result_dict

    @staticmethod
    def parse_csv_to_tuple(value) -> tuple:
        text = PostModelFull.convert_text(value)
        date = PostModelFull.convert_date(value)
        rubrics = PostModelFull.convert_rubrics(value)
        return text, date, rubrics
