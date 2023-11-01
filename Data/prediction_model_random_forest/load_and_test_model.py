"""
    TEST MODEL AGAINST TEST DATASET
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pickle
from sklearn.metrics import accuracy_score
# Load the pre-trained model

model_dir = os.path.join("model", "Random_forest_saved_model")
model_filename = "model_file.p"
model_path = os.path.join(model_dir, model_filename)

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)
# Load the test dataset
test = pd.read_csv(os.path.join("dataset", "test.csv"))

# Ensure the new data is preprocessed in the same way as the training data
scaler = MinMaxScaler()
X_new = test[['speed_kmh', 'segment_max_speed_kmh', 'runtime_sec', 'start_stop_id',
       'end_stop_id', 'distance_m', 'stop_lat', 'stop_lon', 'next_lat',
       'next_lon', 'arrival_hour', 'arrival_minute']]

missing_feature_value = X_new['speed_kmh'].mean()

X_new['avg_route_speed_kmh'] = missing_feature_value

X_new = scaler.fit_transform(X_new)




# Make predictions
predicted_congestion = model.predict(X_new)

# Calculate the accuracy on the training and validation/test sets
accuracy = accuracy_score(test['congestion_level'], predicted_congestion)

print(f'Accuracy - : {accuracy:f}')
location = test[["stop_lat", "stop_lon", "next_lat", "next_lon", "arrival_hour", "arrival_minute"]]
location["congestion_level"] = predicted_congestion

print(location)
# Plot the predicted and actual congestion levels
plt.figure(figsize=(12, 6))
plt.plot(test['congestion_level'], label="Actual Congestion")
plt.plot(predicted_congestion, label="Predicted Congestion")
plt.legend()
plt.xlabel("Time Steps - Location")
plt.ylabel("Congestion Level")
plt.title("Actual vs. Predicted Congestion Levels")
plt.show()

