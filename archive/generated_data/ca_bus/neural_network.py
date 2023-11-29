import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('archive/generated_data/ca_bus/merged_data_5.csv')

# Label encoder for categorical variables
le_route = LabelEncoder()
le_stop = LabelEncoder()
df['route_id'] = le_route.fit_transform(df['route_id'])
df['stop_id'] = le_stop.fit_transform(df['stop_id'])

# Select features and target variable
X = df[['route_id', 'stop_id', 'latitude', 'longitude', 'speed']]
y = df['congestion_level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a simple neural network model
input_shape = [X_train.shape[1]]
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=64, activation='relu', input_shape=input_shape),
    tf.keras.layers.Dense(units=64, activation='relu'),
    tf.keras.layers.Dense(units=1, activation='linear')  # Adjust the number of units
])

# Compile the model
model.compile(optimizer='adam', loss='mae')

# Train the model
model.fit(X_train_scaled, y_train, epochs=15, batch_size=16, validation_split=0.2)

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Round the predicted values to the nearest integer in the range 0 to 4
y_pred_rounded = np.round(y_pred).clip(0, 4).astype(int)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred_rounded)
print(f"Mean Absolute Error: {mae}")

print(y_pred_rounded)

