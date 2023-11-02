import flask
from flask import Flask, jsonify, request, Response
import json
from data_input import data_in
import numpy as np
import pickle
import joblib

from load_model import load_model

def load_models():
    file_name = "model/Random_forest_saved_model/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data[0]
    return model

app = Flask(__name__)

@app.route('/predict_congestion_random_forest', methods=['POST'])
def predict():
    # Load the machine learning model and the scaler
    
    # Extract input data from the JSON request
    request_data = request.get_json()
    
    result_data = load_model(request_data)
    
    # Conver the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

if __name__ == '__main':
    app.run(debug=True)
