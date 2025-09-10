from services.process_files.process_files import get_list_with_all_files_metadata
from services.process_files.config import FOLDER_PATH,METADATA_TOPIC
from services.tools.kafka_producer import publish_message,get_producer_config
from services.tools.my_logger import logger

# Create a list of all metadata and publish it in kafka
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

