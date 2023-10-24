import pandas as pd
import json

# Define the chunk size
chunk_size = 10000

# Load the CSV files into DataFrames
stops_df = pd.read_csv('stops.csv')
stop_times_df = pd.read_csv('stop_times.csv')

# Initialize an empty list to store the results
routes_data = []

# Process the CSV files in chunks
for trips_chunk in pd.read_csv('trips.csv', chunksize=chunk_size):
    # Use the already loaded DataFrames in each iteration
    merged_chunk = trips_chunk.merge(stop_times_df, on='trip_id', how='inner')
    merged_chunk = merged_chunk.merge(stops_df, on='stop_id', how='inner')

    # Filter routes with start_stop_name and end_stop_name not NaN
    filtered_chunk = merged_chunk.dropna(subset=['start_stop_name', 'end_stop_name'])

    # Group by route_id and aggregate the required information for each route in this chunk
    for route_id, route_group in filtered_chunk.groupby('route_id'):
        route_attributes = route_group[['route_id', 'shape_id', 'start_stop_name', 'end_stop_name', 'agency_name']].iloc[0].to_dict()
        
        # Remove duplicate stops based on stop_id
        unique_stops = route_group.drop_duplicates(subset='stop_id')[['stop_id', 'stop_sequence', 'stop_name', 'stop_lat', 'stop_lon']]
        stops_info = unique_stops.to_dict(orient='records')
        
        route_data = {
            'route_id': route_id,
            **route_attributes,
            'stops': stops_info
        }
        routes_data.append(route_data)

# Convert the result to a JSON object
result_json = json.dumps(routes_data, indent=4)

# To save to a file:
with open('lines.json', 'w') as f:
    f.write(result_json)