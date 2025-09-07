import json
from kafka import KafkaProducer


# This makes a Kafka producer.
def get_producer_config():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    print("Producer create successfully!")
    return producer


# This gets the message from Kafka.
def publish_message(producer,topic,message):
    print(f"topic {topic} start sending.")
    producer.send(topic, message)
    print(f"Publish topic {topic} complete.")