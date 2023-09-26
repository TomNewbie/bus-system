import requests
import zipfile
import io
import os

# Get the directory where the Python script is located
script_directory = os.path.dirname(os.path.realpath(__file__))

# Define the URL of the GTFS ZIP file
gtfs_url = "http://download.vrsinfo.de/gtfs/google_transit.zip"

# Define the output directory (same as the script directory)
output_directory = script_directory

# Download the GTFS ZIP file
response = requests.get(gtfs_url)

# Check if the download was successful (HTTP status code 200)
if response.status_code == 200:
    # Open the ZIP file from the response content
    with zipfile.ZipFile(io.BytesIO(response.content), "r") as zip_file:
        # Extract all files from the ZIP archive to the output directory
        zip_file.extractall(output_directory)
    
    print("GTFS data has been successfully downloaded and extracted in the same directory as the script.")
else:
    print(f"Failed to download GTFS data. HTTP Status Code: {response.status_code}")
