import json

from confluent_kafka import Consumer

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "orders_customers-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["customers_orders"])

print("🟢 Consumer is running and subscribed to orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode("utf-8")
        orders_customers = json.loads(value)
        print(f"Received {orders_customers}")
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()
