from pymongo import MongoClient
import time

def perform_mongo_action():
    start = time.time()

    client = MongoClient("mongodb://localhost:27017/")
    db = client["test_db"]
    collection = db["test_collection"]

    # Teste de inserção
    collection.insert_one({"name": "Test", "value": 123})
    print("MongoDB Inserted: ", collection.find_one({"name": "Test"}))

    elapsed = time.time() - start
    print(f"MongoDB action took {elapsed:.2f} seconds")
