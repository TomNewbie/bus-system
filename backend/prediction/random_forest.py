import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle


def run_model(data):
    # Load the pre-trained model
    env = os.getenv("APP_ENVIRONMENT") 
    model = None

    file_name = "model/Random_forest_saved_model/model_file.p"
    with open(file_name, 'rb') as pickled:
        model = pickle.load(pickled)

    df = pd.DataFrame(data)
    df = pd.json_normalize(data, 'segments', meta=['route_id', 'direction_id', 'arrival_hour', 'arrival_minute'])
    df = df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon"]]

    # Ensure the new data is preprocessed in the same way as the training data
    scaler = MinMaxScaler()
    X_new = df[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
    X_new = scaler.fit_transform(X_new)
    predicted_congestion = model.predict(X_new)
    
    df["congestion_level"] = predicted_congestion
    def round_and_constrain(value):
        rounded = round(value)
        return min(max(rounded, 0), 4)

    df["congestion_level"] = df["congestion_level"].apply(round_and_constrain)

    return df[['route_id','direction_id','arrival_hour','arrival_minute','segment_id','start_stop_id',"stop_lat","stop_lon","end_stop_id","next_lat","next_lon",'congestion_level']]
