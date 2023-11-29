'''
TESTING REQUEST SENT TO SERVER
'''
import requests
from data import data_in

# Set the URL of your Flask server
url = "http://127.0.0.1:5000/lstm"

# Send the POST request
response = requests.post(url, json=data_in)

# Extract and print the JSON response
print(response.json())
print(response.status_code)


def test_url(): 
    assert response.status_code == 200, "Server FAILED"
    
def test_response_congestion():
    response_data_list = response.json() 
    assert len(response_data_list) > 0
    for response_data in response_data_list:
        assert response_data.get("congestion_level") is not None

