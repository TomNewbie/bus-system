import pandas as pd
import json

chunk_size = 10000

# Load the CSV files into pandas DataFrames
trips_df = pd.read_csv('trips.csv')
stops_df = pd.read_csv('stops.csv')
stop_times_df = pd.read_csv('stop_times.csv')

stops_data = []

for trips_chunk in pd.read_csv('RMV/Data/trips.csv', chunksize=chunk_size):
    # Inner join trips_df with stop_times_df on trip_id
    merged_chunk = trips_chunk.merge(stop_times_df, on='trip_id', how='inner')

    # Join with stops_df on stop_id
    merged_chunk = merged_chunk.merge(stops_df, on='stop_id', how='inner')

    # Filter trips with start_stop_name and end_stop_name not NaN
    filered_chunk = merged_chunk.dropna(subset=['start_stop_name', 'end_stop_name'])

    # Keep track of visited trip_ids to skip duplicates
    visited_trip_ids = set()

    for stop_id, stop_group in filered_chunk.groupby('stop_id'):
        stop_attributes = stop_group[['stop_name', 'stop_id', 'stop_lat', 'stop_lon']].iloc[0].to_dict()
        
        # Extract trip information for this stop
        trips_info = []
        unique_routes = stop_group.drop_duplicates(subset='route_id')[['route_id','shape_id', 'start_stop_name', 'end_stop_name', 'agency_name']]
        routes_info = unique_routes.to_dict(orient='records')
        
        stop_data = {
            'stop_id': stop_id,
            **stop_attributes,
            'routes': routes_info
        }
        stops_data.append(stop_data)

# Convert the result to a JSON object
result_json = json.dumps(stops_data, indent=4)

# Save the JSON result to a file named 'stops.json'
with open('stops.json', 'w') as f:
    f.write(result_json)