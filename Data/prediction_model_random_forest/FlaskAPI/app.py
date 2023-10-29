import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import  numpy as np
import pickle


def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data[0]
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])

def predict():
    # stub input features
    request_json = request.get_json()
    # Extract input data from JSON request
    input_data = request_json['input']
    model = load_models()

    predictions = []
    for data in input_data:
        # Extract input features from each dictionary
        x = [data["speed_kmh"], data["avg_route_speed_kmh"], data["segment_max_speed_kmh"],
             data["runtime_sec"], data["start_stop_id"], data["end_stop_id"],
             data["distance_m"], data["stop_lat"], data["stop_lon"], data["next_lat"],
             data["next_lon"], data["arrival_hour"], data["arrival_minute"]]

        row_to_predict = np.array(x).reshape(1, -1)

        # Make a prediction
        congestion_level = int(model.predict(row_to_predict)[0])

        # Create a dictionary for the output
        prediction = {
            "route_id": data["route_id"],
            "segment_id": data["segment_id"],
            "congestion_level": congestion_level
        }

        predictions.append(prediction)
    #x = request_json['input']
    
    
    #row_to_predict = np.array(x).reshape(1, -1)
    # load model
    #prediction = int(model.predict(row_to_predict)[0])

    #prediction = int(model.predict(row_to_predict))
    #response = json.dumps({'response': prediction})
    #return response, 200

    response = json.dumps(predictions)
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)