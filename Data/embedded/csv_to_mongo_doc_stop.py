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

# Filter trips with start_stop_name and end_stop_name not NaN
filtered_trips_df = merged_df.dropna(subset=['start_stop_name', 'end_stop_name'])

# Keep track of visited trip_ids to skip duplicates
visited_trip_ids = set()

# Group by stop_id and aggregate the required information for each stop
stops_data = []
for stop_id, stop_group in filtered_trips_df.groupby('stop_id'):
    stop_info = stop_group[['stop_name', 'stop_id', 'stop_lat', 'stop_lon']].iloc[0].to_dict()
    
    # Extract trip information for this stop
    trips_info = []
    for index, row in stop_group.iterrows():
        trip_id = row['trip_id']
        
        # Skip duplicates
        if trip_id in visited_trip_ids:
            continue
        
        visited_trip_ids.add(trip_id)
        
        trip_info = {
            'trip_id': trip_id,
            'route_id': row['route_id'],
            'shape_id': row['shape_id'],
            'start_stop_name': row['start_stop_name'],
            'end_stop_name': row['end_stop_name'],
            'agency_name': row['agency_name']
        }
        trips_info.append(trip_info)
    
    stop_data = {
        'stop_name': stop_info['stop_name'],
        'stop_id': stop_info['stop_id'],
        'stop_lat': stop_info['stop_lat'],
        'stop_lon': stop_info['stop_lon'],
        'trips': trips_info
    }
    stops_data.append(stop_data)

# Convert the result to a JSON object
result_json = json.dumps(stops_data, indent=4)

# Save the JSON result to a file named 'stops.json'
with open('stops.json', 'w') as f:
    f.write(result_json)
