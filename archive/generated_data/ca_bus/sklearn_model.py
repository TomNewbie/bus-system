import pandas as pd
from sklearn.model_selection import train_test_split

# Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

# Create models
# clf = DecisionTreeClassifier()
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
# clf = KNeighborsClassifier(n_neighbors=5)


# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")


# ------------------------------------------------- INCREMENTAL LEARNING --------------------------------------------------------- #


# Simulate new incoming data
df_new_data = pd.read_csv('archive/generated_data/ca_bus/merged_data_5.csv')

# Update the label encoder with new data
df_new_data['route_id'] = le_route.transform(df_new_data['route_id'])
df_new_data['stop_id'] = le_stop.transform(df_new_data['stop_id'])

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