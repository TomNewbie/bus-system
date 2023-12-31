"""
    TEST MODEL AGAINST TEST DATASET
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the pre-trained model
model = keras.models.load_model("backend/prediction_model_lstm/model/LSTM_1_model_saved_model")

# Load the test dataset
test = pd.read_csv("backend/prediction_model_lstm/dataset/pre_processed_data.csv")[0:200]

# Ensure the new data is preprocessed in the same way as the training data
scaler = MinMaxScaler()
X_new = test[
    ['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
X_new = scaler.fit_transform(X_new)

# Define the sequence length (seq_length) used during training
seq_length = 320

# Generate sequences from the new data
X_seq_new = []
num_objects = len(X_new)

for i in range(num_objects):
    start = max(0, i - seq_length + 1)
    sequence = X_new[start:i + 1]
    X_seq_new.append(sequence)

# Pad sequences to ensure consistent length
X_seq_new = pad_sequences(X_seq_new, maxlen=seq_length, dtype='float32', padding='post', truncating='post')

# Assuming 'arrival_time' is the column in the 'test' DataFrame representing the time steps
timestamps = test['arrival_time'].iloc[seq_length - 1:num_objects]

# Make predictions
predicted_congestion = model.predict(X_seq_new)

location = test[
    ['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
location["congestion_level"] = predicted_congestion

def round_and_constrain(value):
    rounded = round(value)
    return min(max(rounded, 0), 4)

# Apply the function to the DataFrame to create the new column
location["congestion_level"] = location["congestion_level"].apply(round_and_constrain)
print(location.info())
print(location)
# Plot the predicted and actual congestion levels
plt.figure(figsize=(24, 6))
plt.plot(location['congestion_level'], label="Predict Congestion")
plt.plot(test['congestion_level'], label="Actual Congestion")
plt.legend()
plt.xlabel("Time Steps - Location")
plt.ylabel("Congestion Level")
plt.title("Actual vs. Predicted Congestion Levels")
plt.show()
