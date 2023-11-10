import time
import requests
from google.protobuf import text_format
from google.protobuf.json_format import MessageToJson
from google.transit import gtfs_realtime_pb2
from concurrent.futures import ThreadPoolExecutor

def stream_gtfs_realtime_data1(feed_url):
    while True:
        try:
            response = requests.get(feed_url)
            if response.status_code == 200:
                feed = gtfs_realtime_pb2.FeedMessage()
                feed.ParseFromString(response.content)

                for entity in feed.entity:
                    if entity.HasField('trip_update'):
                        print("Trip Update:")
                        print(MessageToJson(entity.trip_update))

                    if entity.HasField('vehicle'):
                        print("Vehicle Position:")
                        print(MessageToJson(entity.vehicle))

                    if entity.HasField('alert'):
                        print("Service Alert:")
                        print(MessageToJson(entity.alert))

                time.sleep(60)  # Wait for 60 seconds before fetching data again (adjust as needed)
            else:
                print(f"Failed to fetch GTFS-realtime data. HTTP Status Code: {response.status_code}")
                time.sleep(60)  # Retry after 60 seconds in case of an error
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(60)  # Retry after 60 seconds in case of an error

def fetch_gtfs_realtime_data(feed_url, feed_type):
    try:
        response = requests.get(feed_url)
        if response.status_code == 200:
            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(response.content)

            for entity in feed.entity:
                if feed_type == 'vehiclePositions' and entity.HasField('vehicle'):
                    print("Vehicle Position:")
                    print(MessageToJson(entity.vehicle))
                elif feed_type == 'alerts' and entity.HasField('alert'):
                    print("Service Alert:")
                    print(MessageToJson(entity.alert))
                elif feed_type == 'tripUpdate' and entity.HasField('trip_update'):
                    print("Trip Update:")
                    print(MessageToJson(entity.trip_update))

    except Exception as e:
        print(f"An error occurred for {feed_type}: {str(e)}")

def stream_gtfs_realtime_data(vehicle_positions_url, alerts_url, trip_update_url):
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(fetch_gtfs_realtime_data, vehicle_positions_url, 'vehiclePositions')
        executor.submit(fetch_gtfs_realtime_data, alerts_url, 'alerts')
        executor.submit(fetch_gtfs_realtime_data, trip_update_url, 'tripUpdate')


if __name__ == "__main__":
    vehicle_positions_url = "https://cdn.mbta.com/realtime/VehiclePositions.pb"
    alerts_url = "https://cdn.mbta.com/realtime/Alerts.pb"
    trip_update_url = "https://cdn.mbta.com/realtime/TripUpdates.pb"

    stream_gtfs_realtime_data(vehicle_positions_url, alerts_url, trip_update_url)