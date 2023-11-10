from flask import Flask, request, Response
import lstm
import random_forest
app = Flask(__name__)

@app.route('/lstm', methods=['POST'])
def predict_congestion_lstm():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()
    result_data = lstm.run_model(request_data)

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')


@app.route('/random-forest', methods=['POST'])
def predict():
    # Load the machine learning model and the scaler
    
    # Extract input data from the JSON request
    request_data = request.get_json()
    
    result_data = random_forest.run_model(request_data)
    
    # Conver the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)