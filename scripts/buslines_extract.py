import pandas as pd

# Read the data from the file into a Pandas DataFrame
stop_times = pd.read_csv("stop_times.txt")

stop_times = stop_times[['trip_id','stop_id','arrival_time','departure_time', 'stop_sequence']]

# Read the data from the file into a Pandas DataFrame
stops = pd.read_csv("stops.txt")

stops = stops[['stop_id', 'stop_name', 'stop_lat', 'stop_lon']]

# Merge the DataFrames on the "stopid" column
data = pd.merge(stop_times, stops, on="stop_id", how="inner")

# Read the 'routes.txt' data into a Pandas DataFrame
routes = pd.read_csv("routes.txt")
routes = routes[['route_id', 'route_short_name', 'route_long_name']]

# Remove rows with non-numeric values in 'route_id' column
routes = routes[pd.to_numeric(routes['route_id'], errors='coerce').notnull()]

# Convert 'route_id' to int64
routes['route_id'] = routes['route_id'].astype('int64')

# Read the 'trips.txt' data into a Pandas DataFrame
trips = pd.read_csv("trips.txt")
trips = trips[['route_id', 'trip_id', 'trip_headsign']]

# Sort the 'trips' DataFrame by 'route_id'
trips = trips.sort_values('route_id')

# Merge the 'trips' and 'routes' DataFrames on the 'route_id' column
merged_data = pd.merge(trips, routes, on="route_id")

# Group by 'route_id' and select the first trip in each group
first_trip_in_each_group = merged_data.groupby('route_id').first().reset_index()

# Extract the 'trip_id' values from the 'first_trip_in_each_group' DataFrame into an array
trip_ids_array = first_trip_in_each_group['trip_id'].tolist()

# Use the 'isin' method to filter out rows in 'data' with trip_ids in 'all_trip_ids'
filtered_data = data[data['trip_id'].isin(trip_ids_array)]

filtered_data = filtered_data.sort_values(['trip_id', 'stop_sequence'])

buslines = pd.merge(filtered_data, trips, on="trip_id")

# Export the DataFrame to a JSON file
buslines.to_json("data.json", orient="records", lines=True)

# Print the selected columns, including 'stop_id'
print(buslines[[ 'route_id', 'stop_name', 'arrival_time']])
