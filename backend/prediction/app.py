import os
from flask import Flask, request, Response
from data_transform import transform_data
import random_forest
app = Flask(__name__)

@app.route('/lstm', methods=['POST'])
def predict_congestion_lstm():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()
    result_data = transform_data(request_data)

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

@app.route('/random-forest', methods=['POST'])
def predict_random_forest():
    # Load the machine learning model and the scaler
    
    # Extract input data from the JSON request
    request_data = request.get_json()
    
    result_data = random_forest.run_model(request_data)
    
    # Conver the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

if __name__ == '__main__':
    env = os.getenv("APP_ENVIRONMENT") 
    if env == "production":
        app.run()
    else:
        app.run(debug = True)
