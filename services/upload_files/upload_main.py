from services.upload_files.upload_to_elastic_search import reset_index,load_data_to_elastic
from services.upload_files.upload_to_mongo_db import put_files_to_mongo_db
from services.upload_files.config import METADATA_TOPIC,RESET_INDEX
from services.tools.kafka_consumer import consumer_with_auto_commit
from services.tools.my_logger import logger

# Receives metadata list from Kafka
# loads the metadata to Elasticsearch
# and uploads the files to MongoDB
def run_upload():
    logger.info("---start upload files---")
    if RESET_INDEX:
        reset_index()
    list_files_metadata = consumer_with_auto_commit(METADATA_TOPIC)
    load_data_to_elastic(list_files_metadata)
    put_files_to_mongo_db(list_files_metadata)
    logger.info("Uploading files completed")
    logger.info("---end upload files---")

if __name__ == '__main__':
    run_upload()
