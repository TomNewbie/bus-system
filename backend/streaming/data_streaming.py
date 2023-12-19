import requests
from google.protobuf.json_format import MessageToJson
from google.transit import gtfs_realtime_pb2
from pymongo import MongoClient
from pymongo.server_api import ServerApi

import logging
import time
import json
from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Extract and print the current date
formatted_date = current_date.strftime("%d-%m-%Y")

HOUR_TO_RUN = 10
HOUR_TO_SECOND = 3600
INTERVAL = 30

vehicle_positions_url = "http://www.myridebarrie.ca/gtfs/GTFS_VehiclePositions.pb"

# connect in cloud
uri = "mongodb+srv://gmanbus:VB2yZttIT1rrgtSG@cluster0.q89eazg.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
mongo_client = MongoClient(uri, server_api=ServerApi('1'))
db = mongo_client['gtfs_rt_ca']
collection = db[formatted_date]

def get_data():
    res = requests.get(vehicle_positions_url)
    if res.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(res.content)
        return feed
    else:
        logging.error(f"Failed to retrieve GTFS Realtime data. Status code: {res.status_code}")
        return None


def format_data(res):

    json_data = MessageToJson(res)

    data = json.loads(json_data)
    # Extract data for CSV formatting with handling missing fields
    id_value = extract_value(data, ["id"])
    trip_id = extract_value(data, ["vehicle", "trip", "tripId"])
    schedule_relationship = extract_value(data, ["vehicle", "trip", "scheduleRelationship"])
    route_id = extract_value(data, ["vehicle", "trip", "routeId"])
    direction_id = extract_value(data, ["vehicle", "trip", "directionId"])
    latitude = extract_value(data, ["vehicle", "position", "latitude"])
    longitude = extract_value(data, ["vehicle", "position", "longitude"])
    odometer = extract_value(data, ["vehicle", "position", "odometer"])
    speed = extract_value(data, ["vehicle", "position", "speed"])
    current_stop_sequence = extract_value(data, ["vehicle", "currentStopSequence"])
    current_status = extract_value(data, ["vehicle", "currentStatus"])
    timestamp = extract_value(data, ["vehicle", "timestamp"])
    stop_id = extract_value(data, ["vehicle", "stopId"])
    vehicle_label = extract_value(data, ["vehicle", "vehicle", "label"])

    csv_string = f"{id_value},{trip_id},{schedule_relationship},{route_id},{direction_id},{latitude},{longitude},{odometer},{speed},{current_stop_sequence},{current_status},{timestamp},{stop_id},{vehicle_label}"
    csv_data = dict(zip(["id", "trip_id", "schedule_relationship", "route_id", "direction_id", "latitude", "longitude", "odometer", "speed", "current_stop_sequence", "current_status", "timestamp", "stop_id", "vehicle_label"], csv_string.split(',')))

    return csv_data

def extract_value(data, keys, default=""):
    """
    Recursively extract a value from nested dictionaries.
    Return the value if present, otherwise return the default value.
    """
    current_data = data
    for key in keys:
        if current_data is None:
            return default
        current_data = current_data.get(key)
    return current_data if current_data else default



def add_data_to_mongodb(data):
    for entity in data.entity:
        formated_data = format_data(entity)
        collection.insert_one(formated_data)

def stream_data_to_mongodb():
    total_amount_run = HOUR_TO_RUN * HOUR_TO_SECOND / INTERVAL
    count = 0
    while count < total_amount_run:
        print('====================================')
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        print("Current Time:", formatted_time)
        print("count: ", count)
        try:
            res = get_data()
            if res:
                add_data_to_mongodb(res)               

        except Exception as e:
            logging.error(f'An error occurred: {e}')

        # Sleep for interval amount seconds before stream again
        time.sleep(INTERVAL)
        count = count + 1
    print('done')


if __name__ == "__main__":
    stream_data_to_mongodb()