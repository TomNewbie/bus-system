import pandas as pd
import folium
from folium.plugins import MarkerCluster
# Load data
stops_df = pd.read_csv('D:\Coding\BusManagementProject\RMV\stops.txt')
stop_times_df = pd.read_csv('D:\Coding\BusManagementProject\RMV\stop_times.txt', low_memory=False)

# Choose column
columns_stops = ['stop_id', 'stop_name', 'stop_lat', 'stop_lon', 'location_type']
columns_stop_times = ['trip_id', 'stop_id', 'arrival_time', 'departure_time']


map_center = [stops_df['stop_lat'].mean(), stops_df['stop_lon'].mean()]
map = folium.Map(location=map_center, zoom_start=12)

# Create a MarkerCluster layer
marker_cluster = MarkerCluster().add_to(map)

# Plot stops as markers on the map
for index, row, in stops_df.iterrows():
    folium.CircleMarker([row['stop_lat'], row['stop_lon']], tooltip=row['stop_name'], color='blue', fill=True, fill_color='blue', fill_opacity=1, radius=2).add_to(marker_cluster)
    
map.save('bus_map.html')