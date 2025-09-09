import os
from services.tools.elastic_search import es_instance as es
from services.tools.my_logger import logger

INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")


mapping = {
    "mappings": {
        "properties": {
            "unique_id": {"type": "keyword"},
            "file_create_time":  {"type":"date","format": "yyyy-MM-dd HH:mm" },
            "file_path": {"type": "text"},
            "file_name": {"type": "text"},
            "file_type": {"type": "text"},
            "file_size": {"type": "integer"},
            "transcription": {"type": "text"}
           }
       }
    }


# This function deletes the old index and makes a new one
def reset_index():
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
        logger.info(f"Index '{INDEX_NAME}' deleted.")
    es.indices.create(index=INDEX_NAME, body=mapping)
    logger.info(f"---Index '{INDEX_NAME}' created with mapping.---\n")

# This function loads datadata from  list path files to Elasticsearch
def load_data_to_elastic(list_white_files_metadata):
    inserted = 0
    for file_metadata in list_white_files_metadata:
        es.index(index=INDEX_NAME, document=file_metadata)
        inserted += 1
        logger.debug(f"Inserted {file_metadata['file_name']} to ElasticSearch")
    logger.info(f"---Inserted {inserted} documents to ElasticSearch----\n")
    es.indices.refresh(index=INDEX_NAME)