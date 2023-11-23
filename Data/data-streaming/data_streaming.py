import requests
from google.protobuf.json_format import MessageToJson
from google.transit import gtfs_realtime_pb2
from pymongo import MongoClient
import logging
import time
import json

test_url = "https://gtfsrt.api.translink.com.au/api/realtime/CNS/VehiclePositions"
vehicle_positions_url = "http://www.myridebarrie.ca/gtfs/GTFS_VehiclePositions.pb"
alerts_url = "http://www.myridebarrie.ca/gtfs/GTFS_ServiceAlerts.pb"
trip_update_url = "http://www.myridebarrie.ca/gtfs/GTFS_TripUpdates.pb"

# MongoDB
mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['gtfs_rt']
collection = db['vehicle_positions']


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
    data = []

    for entity in res.entity:
        data1 = MessageToJson(entity)
        data1_dict = json.loads(data1)
        print(data1_dict)
        data.append(data1)

    return data1_dict


def stream_data_to_mongodb():
    while True:
        try:
            res = get_data()
            if res:
                formatted_data = format_data(res)
                collection.insert_one(formatted_data)

        except Exception as e:
            logging.error(f'An error occurred: {e}')

        # Sleep for 5 seconds before stream again
        time.sleep(5)


if __name__ == "__main__":
    stream_data_to_mongodb()