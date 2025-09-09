import os
from services.tools.elastic_search import es_instance as es
from services.tools.my_logger import logger

INDEX_NAME = os.environ.get("INDEX_NAME", "the_muezzin")

def update_transcription_to_elastic_search(file_name,unique_id,text):
    if text!="":
        query_to_match = {
            "match": {
                "unique_id": unique_id
            }
        }
        script_for_update = {
            "source": "ctx._source.transcription = params.text",
            "lang": "painless",
            "params": {
                "text": text
            }
        }
        es.update_by_query(index=INDEX_NAME, body={
            "query": query_to_match,
            "script": script_for_update
        })
        es.indices.refresh(index=INDEX_NAME)
        logger.info(f"{file_name} transcription update to elastic search.")