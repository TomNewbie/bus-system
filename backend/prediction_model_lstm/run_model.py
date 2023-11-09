'''
    TRIGGER THE MODEL
'''
import os
import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf


tf.config.threading.set_inter_op_parallelism_threads(
    1
)


def run_model(transformed_data):
    # LOAD PRE-TRAINED MODEL
    env = os.getenv("APP_ENVIRONMENT") 
    model = None
    if env == "production":
        model = keras.models.load_model("model/LSTM_1_model_saved_model")
    else: 
        model = keras.models.load_model("backend/prediction_model_lstm/model/LSTM_1_model_saved_model")
    
    predicted_congestion = model.predict(transformed_data)
    
    return predicted_congestion