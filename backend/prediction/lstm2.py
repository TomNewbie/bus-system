import pandas as pd
from keras_preprocessing.sequence import pad_sequences
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
import tensorflow as tf

tf.config.threading.set_inter_op_parallelism_threads(1)

def run_lstm_2_model(transformed_data):
    model = keras.models.load_model("model/LSTM_2_model_saved_model")
    predicted_congestion = model.predict(transformed_data)
    scaler = MinMaxScaler(feature_range=(0, 4))
    scaled_congestion = scaler.fit_transform(predicted_congestion.flatten().reshape(-1, 1))
    scaled_congestion = scaled_congestion.flatten()
    return scaled_congestion