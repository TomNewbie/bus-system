import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle


def run_random_forest_model(transformed_data):
    # Load the pre-trained model
    env = os.getenv("APP_ENVIRONMENT") 
    model = None

    file_name = "model/Random_forest_saved_model/model_file.p"
    with open(file_name, 'rb') as pickled:
        model = pickle.load(pickled)

    predicted_congestion = model.predict(transformed_data)
    
    return predicted_congestion

def run_random_forest_model_2(transformed_data):
    # Load the pre-trained model
    env = os.getenv("APP_ENVIRONMENT") 
    model = None

    file_name = "model/Random_forest_saved_model_2/model_file.p"
    with open(file_name, 'rb') as pickled:
        model = pickle.load(pickled)

    predicted_congestion = model.predict(transformed_data)
    
    return predicted_congestion