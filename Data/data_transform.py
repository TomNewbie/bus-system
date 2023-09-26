from gtfs_functions import Feed
import geopandas as gpd
feed = Feed("google_transit.zip", time_windows=[0, 6, 9, 15, 19, 22, 24])

routes = feed.routes
trips = feed.trips
stops = feed.stops
stop_times = feed.stop_times
shapes = feed.shapes

segments_gdf = feed.segments
speeds_data = feed.avg_speeds
segments_gdf.to_file('segment_data.geojson', driver="GeoJSON")
speeds_data.to_file("speeds_data.geojson", driver="GeoJSON")
