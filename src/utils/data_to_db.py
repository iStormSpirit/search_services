import asyncpg


async def insert_data_from_csv_to_db(id, text, created_date, rubrics):
    conn = await asyncpg.connect(user='search_app', password='qwe123',
                                 database='search_db', host='localhost')
    await conn.execute('INSERT INTO post (id, text, created_date, rubrics) VALUES ($1, $2, $3, $4)',
                       id, text, created_date, rubrics)
    await conn.close()
