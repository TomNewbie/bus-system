import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle
import joblib

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data[0]
    return model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Load the machine learning model and the scaler
    model = load_models()
    scaler = joblib.load('models/scaler.pkl')
    
    # Extract input data from the JSON request
    request_json = request.get_json()
    input_data = request_json['input']
    
    # Initialize an empty list to store predictions
    predictions = []
    
    for data in input_data:
        # Extract input features from each dictionary
        x = [
            data["arrival_hour"], data["arrival_minute"], data["stop_lat"], 
            data["stop_lon"], data["next_lat"], data["next_lon"], data["direction_id"]
        ]
        
        # Scale the input features
        row_to_predict = np.array(x).reshape(1, -1)
        user_input_scaled = scaler.transform(row_to_predict)
        
        # Make a prediction
        congestion_level = int(model.predict(user_input_scaled)[0])
        
        # Create a dictionary for the output
        prediction = {
            "route_id": data["route_id"],
            "segment_id": data["segment_id"],
            "congestion_level": congestion_level
        }
        
        # Append the prediction to the list
        predictions.append(prediction)
    
    # Convert the list of predictions to a JSON response
    response = json.dumps(predictions)
    
    return response, 200

if __name__ == '__main':
    app.run(debug=True)
