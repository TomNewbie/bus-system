import os
import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import numpy as np


def run_model(data):
    # Load the pre-trained model
    env = os.getenv("APP_ENVIRONMENT") 
    model = None
    if env == "production":
        model = keras.models.load_model("model/LSTM_1_model_saved_model")
    else: 
        model = keras.models.load_model("backend/prediction_model_lstm/model/LSTM_1_model_saved_model")

    df = pd.DataFrame(data)
    df = pd.json_normalize(data, 'segments', meta=['route_id', 'direction_id', 'arrival_hour', 'arrival_minute'])
    df = df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon", 'runtime_sec']]


    # Extract the hour and minute from the first row
    first_row = df.iloc[0]
    hour = first_row['arrival_hour']
    minute = first_row['arrival_minute']

    # Create a datetime64 object for the first row
    future_time = pd.to_datetime(f"{hour:02d}:{minute:02d}")
    print(future_time)
    calculated_arrival_times = []

    for idx in range(len(df)):
        if idx < 1:
            # For the first row, we've already updated it, so use the provided future_time
            calculated_arrival_times.append(pd.to_datetime(future_time))
        else:
            # For subsequent rows, calculate the 'arrival_time' based on the two previous rows
            previous_arrival_time = calculated_arrival_times[idx - 1]
            previous_runtime = df['runtime_sec'].iloc[idx - 1]
            new_arrival_time = previous_arrival_time + pd.to_timedelta(previous_runtime, unit='s')
            calculated_arrival_times.append(new_arrival_time)

        # print(df['arrival_hour'][idx])
        # print(df['arrival_minute'][idx])

    # Update the 'arrival_time' column with the calculated values
    df['arrival_time'] = calculated_arrival_times
    # -- Create 'arrival_hour' and 'arrival_minute' --
    df['arrival_hour'] = df['arrival_time'].dt.hour
    df['arrival_minute'] = df['arrival_time'].dt.minute



    # Ensure the new data is preprocessed in the same way as the training data
    scaler = MinMaxScaler()
    X_new = df[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
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
    # timestamps = main_data['arrival_time'].iloc[seq_length - 1:num_objects]

    # Make predictions
    predicted_congestion = model.predict(X_seq_new)

    df["congestion_level"] = predicted_congestion

    def round_and_constrain(value):
        rounded = round(value)
        return min(max(rounded, 0), 4)

    df["congestion_level"] = df["congestion_level"].apply(round_and_constrain)

    return df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon",'congestion_level']]

# run_model(300025, 0, "2023-10-25 23:50:00")
