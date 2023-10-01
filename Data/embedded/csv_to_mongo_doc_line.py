import pandas as pd
import json

# Load the CSV files into pandas DataFrames
trips_df = pd.read_csv('trips.csv')
stops_df = pd.read_csv('stops.csv')
stop_times_df = pd.read_csv('stop_times.csv')

# Inner join trips_df with stop_times_df on trip_id
merged_df = trips_df.merge(stop_times_df, on='trip_id', how='inner')

# Join with stops_df on stop_id
merged_df = merged_df.merge(stops_df, on='stop_id', how='inner')

filtered_trips_df = merged_df.dropna(subset=['start_stop_name', 'end_stop_name'])

# Group by trip_id and aggregate the required information for each trip
trips_data = []
for trip_id, trip_group in filtered_trips_df.groupby('trip_id'):
    trip_attributes = trip_group[['route_id', 'trip_id', 'shape_id', 'start_stop_name', 'end_stop_name', 'agency_name']].iloc[0].to_dict()
    
    # Remove duplicate stops based on stop_id
    unique_stops = trip_group.drop_duplicates(subset='stop_id')[['stop_id','arrival_time', 'departure_time', 'stop_sequence', 'stop_name', 'stop_lat', 'stop_lon']]
    stops_info = unique_stops.to_dict(orient='records')
    
    trip_data = {
        'trip_id': trip_id,
        **trip_attributes,
        'stops': stops_info
    }
    trips_data.append(trip_data)

# Convert the result to a JSON object
result_json = json.dumps(trips_data, indent=4)

# To save to a file:
with open('lines.json', 'w') as f:
    f.write(result_json)
