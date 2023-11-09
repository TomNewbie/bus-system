from flask import Flask, request, Response


from data_transform import transform_data

app = Flask(__name__)

@app.route('/predict_congestion_lstm', methods=['POST'])
def predict_congestion():
    # Assuming the data is sent as JSON in the request
    request_data = request.get_json()
    result_data = transform_data(request_data)

    # Convert the result data to JSON
    result_json = result_data.to_json(orient='records')
    return Response(result_json, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)