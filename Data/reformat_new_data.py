import json

with open('data.json', 'r') as file:
    lines = file.readlines()

trips = {}

for line in lines:
    data = json.loads(line)
    trip_id = data['trip_id']

    stop_info = {
        "stop_sequence": data['stop_sequence'],
        "stop_id": data['stop_id'],
        "arrival_time": data['arrival_time'],
        "departure_time": data['departure_time'],
        "stop_lat": data['stop_lat'],
        "stop_lon": data['stop_lon']
    }

    if trip_id in trips:
        trips[trip_id]["sequence"].append(stop_info)
    else:
        trips[trip_id] = {
            "trip_id": trip_id,
            "sequence": [stop_info]
        }


trip_list = list(trips.values())


result = json.dumps(trip_list, indent=4)


with open('reformatted_data.json', 'w') as output_file:
    output_file.write(result)