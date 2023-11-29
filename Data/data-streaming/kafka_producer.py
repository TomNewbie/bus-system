import requests
from kafka import KafkaProducer
from time import sleep
import json
from google.protobuf.json_format import MessageToJson
from google.transit import gtfs_realtime_pb2


# GTFS real time url
url = "http://www.myridebarrie.ca/gtfs/GTFS_VehiclePositions.pb"

# Producing as JSON


# response = requests.get(test_url)
#
# if response.status_code == 200:
#     feed = gtfs_realtime_pb2.FeedMessage()
#     feed.ParseFromString(response.content)
#
#     for entity in feed.entity:
#         content = MessageToJson(entity)
#         content = json.loads(content)
#         # Produce the JSON content to Kafka topic
#         #producer.send('stream1', json.dumps(content).encode('utf-8'))
# else:
#     print(f"Failed to retrieve GTFS Realtime data. Status code: {response.status_code}")

def get_data():
    import requests
    vehicle_positions_url = "https://gtfsrt.api.translink.com.au/api/realtime/CNS/VehiclePositions"

    res = requests.get(url)
    if res.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(res.content)

    return feed

def format_data(res):
    data = []

    for entity in res.entity:
        data1 = MessageToJson(entity)
        #data1_dict = json.loads(data1)
        print(data1)
        data.append(data1)

    return data1
def stream_data():
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             # value_serializer=lambda m: json.dumps(m).encode('ascii'),
                             max_block_ms=5000)
    curr_time = time.time()

    while True:
        # if time.time() > curr_time + 60:
        #     break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('stream1', res.encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

if __name__ == "__main__":
    stream_data()