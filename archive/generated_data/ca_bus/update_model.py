import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

from joblib import dump, load

# Simulate new incoming data
df_new_data = pd.read_csv('archive/generated_data/ca_bus/merged_data_5.csv')

clf = load('archive\generated_data\ca_bus\model.joblib')

# Label encoder for categorical variables
le_route = LabelEncoder()
le_stop = LabelEncoder()
df_new_data['route_id'] = le_route.fit_transform(df_new_data['route_id'])
df_new_data['stop_id'] = le_stop.fit_transform(df_new_data['stop_id'])

# Select features and target variable for new data
X_new_data = df_new_data[['route_id', 'stop_id', 'latitude', 'longitude', 'speed']]
y_new_data = df_new_data['congestion_level']

# Update the model with new data
clf.fit(X_new_data, y_new_data)

# Make predictions on the new test set
y_pred_new_data = clf.predict(X_new_data)

# Evaluate the updated model
accuracy_new_data = accuracy_score(y_new_data, y_pred_new_data)
print(f"Updated Model Accuracy: {accuracy_new_data}")

dump(clf, 'archive\generated_data\ca_bus\model.joblib')