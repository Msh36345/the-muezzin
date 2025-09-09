import os
from services.process_files.process_files import get_list_with_all_files_metadata
from services.tools.kafka_producer import publish_message,get_producer_config
from services.tools.my_logger import logger

FOLDER_PATH = os.getenv("FOLDER_PATH", "podcasts")
METADATA_TOPIC = os.getenv("METADATA_TOPIC","metadata")

def run_process():
    logger.info("---start process files---")
    producer = get_producer_config()
    list_of_files_metadata = get_list_with_all_files_metadata(FOLDER_PATH)
    publish_message(producer, METADATA_TOPIC, list_of_files_metadata)
    producer.flush()
    logger.info("Publish complete.")
    logger.info("---end process files---")

if __name__ == '__main__':
    run_process()

