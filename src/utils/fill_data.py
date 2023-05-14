import asyncio
import uuid

from csv_extractor import extract_data_from_csv
from data_to_db import insert_data_from_csv_to_db


async def main():
    result = extract_data_from_csv()
    for row in result:
        id = uuid.uuid4()
        text = row['text']
        created_date = row['created_date']
        rubrics = row['rubrics']
        await insert_data_from_csv_to_db(id, text, created_date, rubrics)


if __name__ == '__main__':
    asyncio.run(main())
