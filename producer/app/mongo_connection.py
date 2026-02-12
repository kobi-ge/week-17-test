from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


# host = os.getenv("MONGO_HOST", "localhost")
# port= int(os.getenv("MONGO_PORT", 27017))
# username= os.getenv("MONGO_USERNAME", "kobi")
# password= os.getenv("MONGO_PASSWORD", "pass")
#uri = f"mongodb://{username}:{password}@{host}:{port}"
#print(uri)
uri = "mongodb://localhost:27017/"

class MongoManager:
    def __init__(self):
        try:
            self.client = MongoClient(uri)
            self.client.admin.command("ping")
            print("connection established")
            self.db = self.client['suspicios']
            self.collection = self.db['customers_orders']
        except Exception as e:
            print(f"connection failed: {e}")
            return None

    def get(self):
        try:
            results = self.collection.find({}).to_list()
            return results
        except Exception as e:
            print(f"opertion failed: {e}")
            return None
