import json
import os
from kafka import KafkaProducer
from services.tools.my_logger import logger


KAFKA_SERVERS = os.environ.get("KAFKA_SERVERS", 'localhost:9092')

# This makes a Kafka producer.
def get_producer_config():
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVERS],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    logger.info("Producer create successfully!")
    return producer


# This gets the message from Kafka.
def publish_message(producer,topic,message):
    logger.info(f"topic {topic} start sending.")
    producer.send(topic, message)
    logger.info(f"Publish topic {topic} complete.")