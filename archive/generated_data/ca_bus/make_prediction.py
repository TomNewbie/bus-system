import pandas as pd
from joblib import load

from sklearn.preprocessing import LabelEncoder


clf = load('archive\generated_data\ca_bus\model.joblib')

test_data =  pd.read_csv('archive/generated_data/ca_bus/test.csv').drop('congestion_level', axis=1)

le__id = LabelEncoder()
le_id = LabelEncoder()
le_trip_id = LabelEncoder()
le_schedule_relationship = LabelEncoder()
le_route_id = LabelEncoder()
le_direction_id = LabelEncoder()
le_current_status = LabelEncoder()
le_time_stamp = LabelEncoder()
le_stop_sequence = LabelEncoder()

test_data['_id'] = le__id.fit_transform(test_data['_id'])
test_data['id'] = le_id.fit_transform(test_data['id'])
test_data['trip_id'] = le_trip_id.fit_transform(test_data['trip_id'])
test_data['schedule_relationship'] = le_schedule_relationship.fit_transform(test_data['schedule_relationship'])
test_data['route_id'] = le_route_id.fit_transform(test_data['route_id'])
test_data['direction_id'] = le_direction_id.fit_transform(test_data['direction_id'])
test_data['current_status'] = le_current_status.fit_transform(test_data['current_status'])
test_data['timestamp'] = le_time_stamp.fit_transform(test_data['timestamp'])
test_data['current_stop_sequence'] = le_stop_sequence.fit_transform(test_data['current_stop_sequence'])

prediction = clf.predict(test_data)


print(prediction)
