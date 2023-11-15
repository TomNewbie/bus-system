import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from keras_preprocessing.sequence import pad_sequences 
import numpy as np
import matplotlib.pyplot as plt
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from random_forest import run_random_forest_model
from lstm import run_lstm_model 
from xg_boost import run_xgboost_model


dataset = pd.read_csv('backend/prediction/testing/pre_processed_data.csv')

df = dataset[['route_id', 'direction_id', 'arrival_hour', 'arrival_minute', 'segment_id', 'start_stop_id', "stop_lat",
               "stop_lon", "end_stop_id", "next_lat", "next_lon", 'runtime_sec', 'congestion_level']]


X = df[['arrival_hour', 'arrival_minute', 'stop_lat', 'stop_lon', 'next_lat', 'next_lon', 'direction_id']]
y = df['congestion_level']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

# Random Forest Model
scaler_rf = MinMaxScaler()
X_train_rf = scaler_rf.fit_transform(X_train)
X_test_rf = scaler_rf.transform(X_test)
predictions_rf = run_random_forest_model(X_test_rf)

# LSTM Model
scaler_lstm = MinMaxScaler()
X_train_lstm = scaler_lstm.fit_transform(X_train)
X_test_lstm = scaler_lstm.transform(X_test)

seq_length = 320
X_seq_test_lstm = pad_sequences(X_test_lstm, maxlen=seq_length, dtype='float32', padding='post', truncating='post')
X_seq_test_lstm_reshaped = X_seq_test_lstm.reshape((X_seq_test_lstm.shape[0], X_seq_test_lstm.shape[1], 1))
X_seq_test_lstm_reshaped_padded = np.pad(X_seq_test_lstm_reshaped, ((0, 0), (0, 0), (0, 6)), 'constant', constant_values=(0))
predictions_lstm = run_lstm_model(X_seq_test_lstm_reshaped_padded)

# XGBoost
scaler_xg = MinMaxScaler()
X_train_xg = scaler_rf.fit_transform(X_train)
X_test_xg = scaler_rf.transform(X_test)
predictions_xg = run_xgboost_model(X_test_rf)


# Evaluate accuracy
accuracy_rf = accuracy_score(y_test, np.clip(np.round(predictions_rf), 0, 4))
accuracy_lstm = accuracy_score(y_test, np.clip(np.round(predictions_lstm), 0, 4))
accuracy_xg = accuracy_score(y_test, np.clip(np.round(predictions_xg), 0, 4))

# Print the accuracies
print(f"Random Forest Model Accuracy: {accuracy_rf:.2%}")
print(f"LSTM Model Accuracy: {accuracy_lstm:.2%}")
print(f"XGBoost Model Accuracy: {accuracy_xg:.2%}")



# Plotting
labels = ['Random Forest', 'LSTM', 'XGBoost']
accuracies = [accuracy_rf, accuracy_lstm, accuracy_xg]

# Plot accuracy
plt.figure(figsize=(8, 5))
plt.bar(labels, accuracies, color=['blue', 'orange', 'red'])
plt.ylim(0, 1)
plt.ylabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()