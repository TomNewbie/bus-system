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
clf = SVC(kernel='rbf', random_state=42)
# clf = KNeighborsClassifier(n_neighbors=5)


# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")