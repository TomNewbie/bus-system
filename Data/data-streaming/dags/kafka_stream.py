from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToJson
import json

default_args = {
    'owner': 'minhtran',
    'start_date': datetime(2023, 11, 4, 11, 00)
}


# def get_data():
#     import requests
#
#     res = requests.get("https://randomuser.me/api/")
#     res = res.json()
#     res = res['results'][0]
#
#     return res

def get_data():
    import requests
    vehicle_positions_url = "https://gtfsrt.api.translink.com.au/api/realtime/CNS/VehiclePositions"

    res = requests.get(vehicle_positions_url)
    if res.status_code == 200:
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(res.content)

    return feed


# def format_data(res):
#     data = {}
#     location = res['location']
#     data['first_name'] = res['name']['first']
#     data['last_name'] = res['name']['last']
#     data['gender'] = res['gender']
#     data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
#                       f"{location['city']}, {location['state']}, {location['country']}"
#     data['postcode'] = location['postcode']
#     data['email'] = res['email']
#     data['username'] = res['login']['username']
#     data['dob'] = res['dob']['date']
#     data['registered_date'] = res['registered']['date']
#     data['phone'] = res['phone']
#     data['picture'] = res['picture']['medium']
#
#     return data
def format_data(res):
    data = []

    for entity in res.entity:
        if entity.HasField('vehicle'):

            data1 = MessageToJson(entity.vehicle)
            data1_dict = json.loads(data1)
            # print(data1)

            trip_info = None
            position_info = None
            if 'trip' in data1_dict and 'position' in data1_dict and 'stopId' in data1_dict:
                trip_info = data1_dict['trip']
                position_info = data1_dict['position']
                data2 = {
                    'trip_id': trip_info.get('tripId', None),
                    'route_id': trip_info.get('routeId', None),
                    'latitude': position_info.get('latitude', None),
                    'longitude': position_info.get('longitude', None),
                    'stop_id': data1_dict.get('stopId', None)
                }
                data.append(data2)

    return data


def stream_data():
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60:
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue


# with DAG('user_automation',
#          default_args=default_args,
#          schedule='@daily',
#          catchup=False) as dag:
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=stream_data
#     )



dag = DAG(
    'user_automation',
    default_args=default_args,
    description='My User Automation DAG',
    schedule_interval='@daily',
)

task = PythonOperator(
    task_id='my_python_task2',
    python_callable=stream_data,
    dag=dag,
)