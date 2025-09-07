import os
from services.tools.kafka_producer import publish_message,get_producer_config
from services.process_files.process_files import get_list_with_all_files_metadata

folder_path = os.getenv("FOLDER_PATH", "podcasts")
metadata_topic = os.getenv("METADATA_TOPIC","metadata")


if __name__ == '__main__':
    producer = get_producer_config()
    list_of_files_metadata = get_list_with_all_files_metadata(folder_path)
    publish_message(producer, metadata_topic, list_of_files_metadata)
    producer.flush()
    print("Publish complete.")
