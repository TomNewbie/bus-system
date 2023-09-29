#!/bin/bash

# Directory where CSV files are located
csv_directory="/tmp/data"

# MongoDB configuration
mongo_db=${MONGO_INITDB_DATABASE}
mongo_username=${MONGO_INITDB_ROOT_USERNAME}
mongo_password=${MONGO_INITDB_ROOT_PASSWORD}

# Check if the directory exists
if [ ! -d "$csv_directory" ]; then
  echo "Directory $csv_directory does not exist."
  exit 1
fi

mongod --auth

# Iterate over each CSV file in the directory
for csv_file in "$csv_directory"/*.csv; do
  if [ -f "$csv_file" ]; then
    echo "Processing file: $csv_file"

    # Get the base filename (excluding the directory and extension)
    base_filename=$(basename "$csv_file" .csv)
    collection_name="${base_filename}"

    # Run the mongoimport command for each CSV file
    mongoimport -d "$mongo_db" -c "$collection_name" --file "$csv_file" \
      --type=csv -u "$mongo_username" -p "$mongo_password" \
      --headerline --authenticationDatabase=admin

    echo "Import completed for file: $csv_file into collection: $collection_name"
  fi
done
