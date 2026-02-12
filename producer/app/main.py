from kafka_publisher import connection, load_from_mongo

def main():
    try:
        load_from_mongo()
    except Exception as e:
        print(f"error: {e}")
