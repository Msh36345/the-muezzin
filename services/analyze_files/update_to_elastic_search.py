import os
from services.tools.elastic_search import es_instance as es
from services.tools.my_logger import logger

INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")

def update_transcription_to_elastic_search(file_data):
    query_to_match = {
        "match": {
            "unique_id": file_data['unique_id']
        }
    }

    script_source = [
        "ctx._source.transcription = params.text;",
        "ctx._source.bds_percent = params.bds_percent;",
        "ctx._source.is_bds = params.is_bds;",
        "ctx._source.bds_threat_level = params.bds_threat_level;"
    ]

    params = {
        "text": file_data['text'],
        "bds_percent": file_data['bds_percent'],
        "is_bds": file_data['is_bds'],
        "bds_threat_level": file_data['bds_threat_level']
    }

    script_for_update = {
    "source": " ".join(script_source),
    "lang": "painless",
    "params": params
    }

    es.update_by_query(index=INDEX_NAME, body={
        "query": query_to_match,
        "script": script_for_update
    })
    es.indices.refresh(index=INDEX_NAME)
    logger.info(f"{file_data['file_name']} update to elastic search.\n")