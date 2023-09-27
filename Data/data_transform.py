from gtfs_functions import Feed
import geopandas as gpd
feed = Feed("google_transit.zip", time_windows=[0, 6, 9, 15, 19, 22, 24])



line_freq = feed.lines_freq
stop_freq = feed.stops_freq
segments_gdf = feed.segments
speeds_data = feed.avg_speeds

#segments_gdf.to_file('segment_data.geojson', driver="GeoJSON")
#speeds_data.to_file("speeds_data.geojson", driver="GeoJSON")
segments_gdf.to_csv("segment_data.csv")
speeds_data.to_csv("speeds_data.csv")
line_freq.to_csv("line_freq.csv")
stop_freq.to_csv("stop_freq.csv")