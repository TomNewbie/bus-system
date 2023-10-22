import pandas as pd
import json

# Load the JSON data from a file into a Pandas DataFrame
input_file = "segments.json"  # Replace with the path to your JSON input file
with open(input_file) as f:
    data = json.load(f)
df = pd.json_normalize(data)  # Flatten the nested structure

# Group the DataFrame by 'properties.route_id' and 'properties.shape_id'
grouped = df.groupby(['properties.route_id', 'properties.shape_id'])

# Create a dictionary to store the grouped data
grouped_data = {}

# Iterate through the groups and store them in the dictionary
for (route_id, shape_id), group in grouped:
    # Convert the tuple keys to strings
    route_id_str = str(route_id)
    shape_id_str = str(shape_id)
    if route_id_str not in grouped_data:
        grouped_data[route_id_str] = {}
    if shape_id_str not in grouped_data[route_id_str]:
        grouped_data[route_id_str][shape_id_str] = group.to_dict(orient='records')

# Sort the objects within each route by 'properties.stop_sequence'
for route_id, shapes in grouped_data.items():
    for shape_id, shape_data in shapes.items():
        shapes[shape_id] = sorted(shape_data, key=lambda item: item['properties.stop_sequence'])

# Keep only the objects with the largest number of elements for each route_id
final_grouped_data = {}
for route_id, shapes in grouped_data.items():
    max_shape_id = max(shapes, key=lambda k: len(shapes[k]))
    final_grouped_data[route_id] = shapes[max_shape_id]

# Flatten the data into a list of dictionaries with the desired structure
flattened_data = []
for route_id, shape_data in final_grouped_data.items():
    for item in shape_data:
        flattened_item = {
            "type": "Feature",
            "properties": {
                "shape_id": item["properties.shape_id"],
                "route_id": item["properties.route_id"],
                "route_name": item["properties.route_name"],
                "direction_id": item["properties.direction_id"],
                "stop_sequence": item["properties.stop_sequence"],
                "segment_name": item["properties.segment_name"],
                "start_stop_name": item["properties.start_stop_name"],
                "end_stop_name": item["properties.end_stop_name"],
                "segment_id": item["properties.segment_id"],
                "start_stop_id": item["properties.start_stop_id"],
                "end_stop_id": item["properties.end_stop_id"],
                "distance_m": item["properties.distance_m"],
            },
            "geometry": {
                "type": "LineString",
                "coordinates": item["geometry.coordinates"]
            }
        }
        flattened_data.append(flattened_item)

# Define the output file path as "flattened_data.json"
output_file = "flattened_data.json"

flattened_data = json.dumps(flattened_data, indent=2)

# Write the formatted data to the output file in JSON format
with open(output_file, 'w') as outfile:
  outfile.write(flattened_data)

print(f"Formatted data has been written to {output_file}")






