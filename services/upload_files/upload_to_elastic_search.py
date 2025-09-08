from services.tools.elastic_search import es_instance as es,INDEX_NAME
from services.tools.my_logger import logger
from datetime import datetime
mapping = {
    "mappings": {
        "properties": {
            "unique_id": {"type": "keyword"},
            "file_create_time":  {"type":"date","format": "yyyy-MM-dd HH:mm" },
            "file_path": {"type": "text"},
            "file_name": {"type": "text"},
            "file_type": {"type": "text"},
            "file_size": {"type": "integer"}
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

# This function loads data from a file to Elasticsearch
def load_data_to_elastic(list_white_files_metadata):
    inserted = 0
    for file_metadata in list_white_files_metadata:
        es.index(index=INDEX_NAME, document=file_metadata)
        inserted += 1
        if inserted%10==0:
            logger.info(f"Inserted {inserted} documents")
    logger.info(f"---Inserted {inserted} documents----\n")
    es.indices.refresh(index=INDEX_NAME)