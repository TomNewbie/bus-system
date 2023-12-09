import os
from flask import Flask, request, Response
from run_model import run_model
import random_forest
app = Flask(__name__)

# LSTM
@app.route('/lstm', methods=['POST'])
def predict_congestion_lstm():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()
    result_data = run_model(request_data, "lstm")

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

# LSTM2
@app.route('/lstm-2', methods=['POST'])
def predict_congestion_lstm_2():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()
    result_data = run_model(request_data, "lstm2")

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')


# RANDOM FOREST
@app.route('/random-forest', methods=['POST'])
def predict_random_forest():
    request_data = request.get_json()
    
    result_data = run_model(request_data, "random_forest")
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

if __name__ == '__main__':
    env = os.getenv("APP_ENVIRONMENT") 
    if env == "production":
        app.run()
    else:
        app.run(debug = True)
