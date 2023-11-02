import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pickle
from sklearn.metrics import accuracy_score

# Load the pre-trained model

model_path = os.path.join('Random_forest_saved_model', 'model_file.p')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# -- Load the MinMaxScaler used during training --
scaler = MinMaxScaler()

# -- Load the training data --
training_data = pd.read_csv(os.path.join("dataset", "clean_data.csv"))

#missing_feature_value = training_data['speed_kmh'].mean()

#training_data['missing_feature'] = missing_feature_value
# -- Fit the scaler with the training data --
scaler.fit(training_data[['speed_kmh', 'avg_route_speed_kmh', 'segment_max_speed_kmh', 'runtime_sec', 'start_stop_id',
       'end_stop_id', 'distance_m', 'stop_lat', 'stop_lon', 'next_lat',
       'next_lon', 'arrival_hour', 'arrival_minute']])



# -- Function to get congestion level based on user input --
def predict_congestion(user_input):
    # Extract user input
    stop_lat, stop_lon, next_lat, next_lon, arrival_hour, arrival_minute = user_input

    missing_speed_kmh = training_data['speed_kmh'].mean()
    missing_segment_max_speed_kmh = training_data['segment_max_speed_kmh'].mean()
    missing_runtime_sec = training_data['runtime_sec'].mean()
    missing_distance_m = training_data['distance_m'].mean()
    missing_distance_m = training_data['distance_m'].mean()
    missing_distance_m = training_data['distance_m'].mean()
    missing_avg_route_speed_kmh = training_data['avg_route_speed_kmh'].mean()



    # Create a feature vector using the user input
    user_features = np.array([[missing_speed_kmh, missing_avg_route_speed_kmh, missing_segment_max_speed_kmh, missing_runtime_sec, 0, 0, missing_distance_m ,arrival_hour, arrival_minute, stop_lat, stop_lon, next_lat, next_lon]])

    # Normalize the user input using the fitted scaler
    user_features = scaler.transform(user_features)

    # Use the model to predict the congestion level
    predicted_congestion = model.predict(user_features)

    return predicted_congestion[0]


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