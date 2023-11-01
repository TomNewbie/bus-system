import requests

# Set the URL of your Flask server
url = "http://127.0.0.1:5000/predict_congestion_lstm"

# Define the data to send in the request
data = {
    "route_id": 300025,
    "direction_id": 1,
    "arrival_hour": 3,
    "arrival_minute": 50,
    "segments": [
        {
            "segment_id": "111-222",
            "start_stop_id": 111,
            "stop_lat": 55.55,
            "stop_lon": 55.55,
            "end_stop_id": 222,
            "next_lat": 66.66,
            "next_lon": 66.66
        },
        {
            "segment_id": "222-333",
            "start_stop_id": 222,
            "stop_lat": 66.66,
            "stop_lon": 66.66,
            "end_stop_id": 333,
            "next_lat": 77.77,
            "next_lon": 77.77,
        }
    ]
}


# Send the POST request
response = requests.post(url, json=data)

# Extract and print the JSON response
print(response.json())