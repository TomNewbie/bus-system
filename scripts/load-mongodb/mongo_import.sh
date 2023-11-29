#!/bin/bash

mongod --auth
# Directory containing the JSON files
json_dir="/tmp/embedded"

# MongoDB connection details
mongo_db="${MONGO_INITDB_DATABASE}"
mongo_username="${MONGO_INITDB_ROOT_USERNAME}"
mongo_password="${MONGO_INITDB_ROOT_PASSWORD}"

# Loop through each JSON file in the directory
for json_file in "$json_dir"/*.json; do
    # Extract the base name of the JSON file (without the extension)
    base_name=$(basename "${json_file%.*}")
    collection_name="$base_name"

    # Execute mongoimport command for each JSON file
    mongoimport -d "$mongo_db" -c "$collection_name" --file "$json_file" --jsonArray -u "$mongo_username" -p "$mongo_password" --authenticationDatabase admin
done
