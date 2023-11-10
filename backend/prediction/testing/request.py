'''
    TESTING REQUEST SENT TO SERVER
'''
import requests
from data import data_in
# Set the URL of your Flask server
url = "http://127.0.0.1:5000/predict_congestion_lstm"


# Send the POST request
response = requests.post(url, json=data_in)

# Extract and print the JSON response
print(response.json())