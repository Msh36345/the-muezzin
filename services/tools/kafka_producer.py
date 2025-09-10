import json
from kafka import KafkaProducer
from services.tools.my_logger import logger
from services.tools.config import KAFKA_SERVERS


# This makes a Kafka producer.
def get_producer_config():
    producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVERS],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    logger.info("Producer create successfully!")
    return producer


# This publishes the message to Kafka.
def publish_message(producer,topic,message):
    logger.info(f"topic {topic} start sending.")
    producer.send(topic, message)
    logger.info(f"Publish topic {topic} complete.")