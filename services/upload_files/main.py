import os
from services.upload_files.upload_to_elastic_search import reset_index,load_data_to_elastic
from services.tools.kafka_consumer import consumer_with_auto_commit
from services.tools.my_logger import logger


METADATA_TOPIC = os.getenv("METADATA_TOPIC","metadata")

if __name__ == '__main__':
    reset_index()
    list_files_mrtadata = consumer_with_auto_commit(METADATA_TOPIC)
    load_data_to_elastic(list_files_mrtadata)
