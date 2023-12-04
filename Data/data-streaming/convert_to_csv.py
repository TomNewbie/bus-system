import pandas as pd
from pymongo import MongoClient
from pymongo.server_api import ServerApi


# Connect to MongoDB
# mongo_client = MongoClient('mongodb://localhost:27017')
uri = "mongodb+srv://gmanbus:VB2yZttIT1rrgtSG@cluster0.q89eazg.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client['gtfs_rt_ca'] # Replace 'your_database' with your actual database name
collection = db['vehicle_positions'] # Replace 'your_collection' with your actual collection name

# Fetch data from MongoDB
cursor = collection.find()

# Convert MongoDB cursor to a Pandas DataFrame
df = pd.DataFrame(list(cursor))

# Specify the CSV file path
csv_file_path = 'output.csv'

# Export DataFrame to CSV
df.to_csv(csv_file_path, index=False)

print(f"Data exported to CSV file: {csv_file_path}")
