from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")


def es_info():
    return es.info().body


def refresh_index(index: str):
    return es.indices.refresh(index=index)


def first_create_index():
    mappings = {
        "properties": {
            "id": {"type": "integer"},
            "text": {"type": "text", "analyzer": "standard"},
        }
    }

    es.indices.create(index="post_text", mappings=mappings)


def create_data_es(idx_db: str, text: str):
    doc = {
        "id": idx_db,
        "title": f'{text}',
    }
    es.index(index="post_text", id=idx_db, document=doc)


def search_data_es(index: str, text: str, size: int = 5, first_idx: int = 0):
    query = {
        "query": {
            "match": {
                "title": text
            }
        }
    }
    result = es.search(index=index, body=query, size=size, from_=first_idx)
    return result


def delete_data_es(index: str, id_ex: str):
    try:
        es.delete(index=index, id=id_ex)
        return f'obj from {index} with id {id_ex} was deleted'
    except Exception as ex:
        return f'delete_data_es error{ex}'


def main():
    # first_create_index()
    es_info()
    # text = 'this text number 5'
    # result = search_data_es('post_text', text=text, size=100)
    # for hit in result["hits"]["hits"]:
    #     print(hit["_source"])


if __name__ == '__main__':
    main()
