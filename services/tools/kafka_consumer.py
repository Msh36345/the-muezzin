import json
import os
from kafka import KafkaConsumer
from services.tools.my_logger import logger


KAFKA_SERVERS = os.environ.get("KAFKA_SERVERS", 'localhost:9092')

# This makes a Kafka consumer.
def get_consumer_events(topic):
    logger.info("Consumer create successfully!")
    consumer = KafkaConsumer(topic,
                             value_deserializer=lambda m: json.loads(m.decode('ascii')),
                             bootstrap_servers=[KAFKA_SERVERS],
                             consumer_timeout_ms=10000)
    return consumer

def consumer_with_auto_commit(topic):
    message_value = ""
    messages = get_consumer_events(topic)
    for message in messages:
        message_value = message.value
    logger.info(f"List contents {len(message_value)} files.")
    logger.debug(message_value)
    return message_value