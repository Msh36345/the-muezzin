import json
from kafka import KafkaConsumer


# This makes a Kafka consumer.
def get_consumer_events(topic):
    print("Consumer create successfully!")
    consumer = KafkaConsumer(topic,
                             value_deserializer=lambda m: json.loads(m.decode('ascii')),
                             bootstrap_servers=['localhost:9092'],
                             consumer_timeout_ms=10000)
    return consumer

def consumer_with_auto_commit(topic):
    message_value = ""
    messages = get_consumer_events(topic)
    for message in messages:
        message_value = message.value
    print(f"List contents {len(message_value)} files.")
    return message_value

if __name__ == '__main__':
    consumer_with_auto_commit("metadata")