import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# -- Load trained LSTM model --
model = keras.models.load_model("model\\LSTM_1_model_saved_model")

# -- Load the MinMaxScaler used during training --
scaler = MinMaxScaler()

# -- Load the training data --
training_data = pd.read_csv("dataset\\pre_processed_data.csv")

# -- Fit the scaler with the training data --
scaler.fit(training_data[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'speed_kmh',
        'segment_max_speed_kmh', 'runtime_sec', 'direction_id', 'distance_m']])


# -- Function to get congestion level based on user input --
def predict_congestion(user_input):
    # Extract user input
    stop_lat, stop_lon, next_lat, next_lon, arrival_hour, arrival_minute = user_input

    # Create a feature vector using the user input
    user_features = np.array([[arrival_hour, arrival_minute, stop_lat, stop_lon, stop_lat, stop_lon, next_lat, next_lon, 0, 0, 0]])

    # Normalize the user input using the fitted scaler
    user_features = scaler.transform(user_features)

    # Reshape the feature vector to match the model's input shape
    user_features = user_features.reshape((1, user_features.shape[0], user_features.shape[1]))

    # Use the model to predict the congestion level
    predicted_congestion = model.predict(user_features)

    return predicted_congestion[0][0]


# -- Get user input --
stop_lat = float(input("Enter stop latitude: "))
stop_lon = float(input("Enter stop longitude: "))
next_lat = float(input("Enter next stop latitude: "))
next_lon = float(input("Enter next stop longitude: "))
arrival_hour = int(input("Enter arrival hour: "))
arrival_minute = int(input("Enter arrival minute: "))

# -- Make a prediction --
user_input = [stop_lat, stop_lon, next_lat, next_lon, arrival_hour, arrival_minute]
predicted_congestion = predict_congestion(user_input)

print(f"Predicted Congestion Level: {predicted_congestion}")
