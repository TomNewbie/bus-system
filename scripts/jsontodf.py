import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

# Define the data to send in the request
data = {
    "route_id": 300025,
    "direction_id": 1,
    "arrival_hour": 3,
    "arrival_minute": 50,
    "segments": [
        {
            "segment_id": "111-222",
            "start_stop_id": 111,
            "stop_lat": 55.55,
            "stop_lon": 55.55,
            "end_stop_id": 222,
            "next_lat": 66.66,
            "next_lon": 66.66
        },
        {
            "segment_id": "222-333",
            "start_stop_id": 222,
            "stop_lat": 66.66,
            "stop_lon": 66.66,
            "end_stop_id": 333,
            "next_lat": 77.77,
            "next_lon": 77.77,
        }
    ]
}


df = pd.DataFrame(data)
df = pd.json_normalize(data, 'segments', meta=['route_id', 'direction_id', 'arrival_hour', 'arrival_minute'])
df = df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon"]]


# Load the pre-trained model
model = keras.models.load_model("backend/prediction_model_lstm/model/LSTM_1_model_saved_model")

df = pd.DataFrame(data)
df = pd.json_normalize(data, 'segments', meta=['route_id', 'direction_id', 'arrival_hour', 'arrival_minute'])



# Ensure the new data is preprocessed in the same way as the training data
scaler = MinMaxScaler()
X_new = df[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
X_new = scaler.fit_transform(X_new)


# Define the sequence length (seq_length) used during training
seq_length = 64

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

print(df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon",'congestion_level']])