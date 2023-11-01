from flask import Flask, request, Response


from run_model import run_model

app = Flask(__name__)

@app.route('/predict_congestion_lstm', methods=['POST'])
def predict_congestion():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()

    # Extract 'route_id', 'direction_id', and 'future_time' from the request
    # route_id = request_data.get('route_id')
    # direction_id = request_data.get('direction_id')
    # future_time = request_data.get('future_time')

    # Your existing script here
    # ...

    # Replace this with your script's logic
    # Load the pre-trained model and process the data
    result_data = run_model(request_data)

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)