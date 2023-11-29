from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# MongoDB 
mongo_client = MongoClient('mongodb://localhost:27017') 
db = mongo_client['gtfs_rt']
collection = db['vehicle_positions']

# Kafka Consumer settings
consumer = KafkaConsumer('stream1',
                         bootstrap_servers=['localhost:9092']
                         # value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    gtfs_realtime_data_str = message.value.decode('utf-8')
    try:
        # Parse the JSON string into a Python dictionary
        gtfs_realtime_data_dict = json.loads(gtfs_realtime_data_str)

        # Insert data into MongoDB
        collection.insert_one(gtfs_realtime_data_dict)

        print("Data inserted into MongoDB:", gtfs_realtime_data_dict)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")