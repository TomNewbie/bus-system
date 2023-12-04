import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['gtfs_rt'] # Replace 'your_database' with your actual database name
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
