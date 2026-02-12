import json
import uuid
from confluent_kafka import Producer
import time

from mongo_connection import MongoManager

connection = MongoManager()



producer_config = {
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")


def load_from_mongo():
    data = connection.get()
    for element in data:
        element['_id'] = str(element['_id'])
        value = json.dumps(element).encode("utf-8")
        time.sleep(0.5)

        producer.produce(
            topic="customers_orders",
            value=value,
            callback=delivery_report
        )

        producer.flush()
