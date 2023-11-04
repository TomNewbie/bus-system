'''
    CORE FUNCTION OF LSTM SERVER
'''
import os
import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import numpy as np


def run_model(data):
    # LOAD PRE-TRAINED MODEL
    env = os.getenv("APP_ENVIRONMENT") 
    model = None
    if env == "production":
        model = keras.models.load_model("model/LSTM_1_model_saved_model")
    else: 
        model = keras.models.load_model("backend/prediction_model_lstm/model/LSTM_1_model_saved_model")

    # CONVERT data INTO DATAFRAME FORMAT
    df = pd.DataFrame(data)
    df = pd.json_normalize(data, 'segments', meta=['route_id', 'direction_id', 'arrival_hour', 'arrival_minute'])
    df = df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon", 'runtime_sec']]


    # MODIFY TIMELINE
    first_row = df.iloc[0]
    hour = first_row['arrival_hour']
    minute = first_row['arrival_minute']

    future_time = pd.to_datetime(f"{hour:02d}:{minute:02d}")
    print(future_time)
    calculated_arrival_times = []

    for idx in range(len(df)):
        if idx < 1:
            calculated_arrival_times.append(pd.to_datetime(future_time))
        else:
            previous_arrival_time = calculated_arrival_times[idx - 1]
            previous_runtime = df['runtime_sec'].iloc[idx - 1]
            new_arrival_time = previous_arrival_time + pd.to_timedelta(previous_runtime, unit='s')
            calculated_arrival_times.append(new_arrival_time)

    df['arrival_time'] = calculated_arrival_times
    df['arrival_hour'] = df['arrival_time'].dt.hour
    df['arrival_minute'] = df['arrival_time'].dt.minute


    # SCALE DATAFRAME
    scaler = MinMaxScaler()
    X_new = df[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
    X_new = scaler.fit_transform(X_new)

    # MAKE PREDICTION
    seq_length = 320
    X_seq_new = []
    num_objects = len(X_new)
    
    for i in range(num_objects):
        start = max(0, i - seq_length + 1)
        sequence = X_new[start:i + 1]
        X_seq_new.append(sequence)
        
    X_seq_new = pad_sequences(X_seq_new, maxlen=seq_length, dtype='float32', padding='post', truncating='post')
    
    predicted_congestion = model.predict(X_seq_new)
    
    df["congestion_level"] = predicted_congestion

    # ROUND PREDICTION VALUE TO INTEGER 0 -> 4
    def round_and_constrain(value):
        rounded = round(value)
        return min(max(rounded, 0), 4)
    df["congestion_level"] = df["congestion_level"].apply(round_and_constrain)

    
    return df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon",'congestion_level']]


