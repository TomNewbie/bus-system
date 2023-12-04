import pandas as pd
from sklearn.model_selection import train_test_split

# Models Classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


# Models Regressors
# from sklearn.svm import SVR 
  
  
  
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

from joblib import dump

# Read the dataset
df = pd.read_csv('archive/generated_data/ca_bus/part_1.csv')


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

df['_id'] = le__id.fit_transform(df['_id'])
df['id'] = le_id.fit_transform(df['id'])
df['trip_id'] = le_trip_id.fit_transform(df['trip_id'])
df['schedule_relationship'] = le_schedule_relationship.fit_transform(df['schedule_relationship'])
df['route_id'] = le_route_id.fit_transform(df['route_id'])
df['direction_id'] = le_direction_id.fit_transform(df['direction_id'])
df['current_status'] = le_current_status.fit_transform(df['current_status'])
df['timestamp'] = le_time_stamp.fit_transform(df['timestamp'])
df['current_stop_sequence'] = le_stop_sequence.fit_transform(df['current_stop_sequence'])

# Select features and target variable
X = df[['_id', 'id', 'trip_id', 'schedule_relationship', 'route_id',
       'direction_id', 'latitude', 'longitude', 'odometer', 'speed',
       'current_stop_sequence', 'current_status', 'timestamp', 'stop_id'
       ]]


y = df['congestion_level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=42)

# Create models
# clf = DecisionTreeClassifier()
clf = RandomForestClassifier(n_estimators=100, random_state=42)
# clf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
# clf = KNeighborsClassifier(n_neighbors=5)

# clf = SVR(kernel='rbf') 

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)
# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

dump(clf, 'archive\generated_data\ca_bus\model.joblib')