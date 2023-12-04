import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load

# Simulate new incoming data
df_new_data = pd.read_csv('archive/generated_data/ca_bus/part_2.csv')

clf = load('archive\generated_data\ca_bus\model.joblib')

# Label encoder for categorical variables
# Label encoder for categorical variables
le__id = LabelEncoder()
le_id = LabelEncoder()
le_trip_id = LabelEncoder()
le_schedule_relationship = LabelEncoder()
le_route_id = LabelEncoder()
le_direction_id = LabelEncoder()
le_current_status = LabelEncoder()
le_time_stamp = LabelEncoder()
le_stop_sequence = LabelEncoder()


df_new_data['_id'] = le__id.fit_transform(df_new_data['_id'])
df_new_data['id'] = le_id.fit_transform(df_new_data['id'])
df_new_data['trip_id'] = le_trip_id.fit_transform(df_new_data['trip_id'])
df_new_data['schedule_relationship'] = le_schedule_relationship.fit_transform(df_new_data['schedule_relationship'])
df_new_data['route_id'] = le_route_id.fit_transform(df_new_data['route_id'])
df_new_data['direction_id'] = le_direction_id.fit_transform(df_new_data['direction_id'])
df_new_data['current_status'] = le_current_status.fit_transform(df_new_data['current_status'])
df_new_data['timestamp'] = le_time_stamp.fit_transform(df_new_data['timestamp'])
df_new_data['current_stop_sequence'] = le_stop_sequence.fit_transform(df_new_data['current_stop_sequence'])

# Select features and target variable
X_new_data = df_new_data[['_id', 'id', 'trip_id', 'schedule_relationship', 'route_id',
       'direction_id', 'latitude', 'longitude', 'odometer', 'speed',
       'current_stop_sequence', 'current_status', 'timestamp', 'stop_id'
       ]]


y_new_data = df_new_data['congestion_level']

# Update the model with new data
clf.fit(X_new_data, y_new_data)

# Make predictions on the new test set
y_pred_new_data = clf.predict(X_new_data)

# Evaluate the updated model
accuracy_new_data = accuracy_score(y_new_data, y_pred_new_data)
print(f"Updated Model Accuracy: {accuracy_new_data}")

dump(clf, 'archive\generated_data\ca_bus\model.joblib')