# Data README

This document provides an overview of the dataset used for the Bus Congestion Prediction Project. The dataset consists of several CSV files that contain information related to bus agencies, routes, stops, shapes, trip schedules, and various other attributes.

## Files

1. `agency.csv`
   - Contains information about bus agencies.
   - Columns:
     - `agency_id`: Unique identifier for the agency.
     - `agency_name`: Name of the agency.

2. `routes.csv`
   - Contains details about bus routes.
   - Columns:
     - `route_id`: Unique identifier for the route.
     - `agency_id`: Identifier of the agency associated with the route.
     - `route_short_name`: Short name for the route.
     - `route_long_name`: Long name for the route.

3. `shapes.csv`
   - Provides information about the shape of routes.
   - Columns:
     - `shape_id`: Unique identifier for the shape.
     - `shape_pt_lat`: Latitude of a shape point.
     - `shape_pt_lon`: Longitude of a shape point.
     - `shape_pt_sequence`: Sequence order of shape points.
     - `shape_dist_traveled`: Distance traveled along the shape.

4. `stop_times.csv`
   - Contains details of stop times for trips.
   - Columns:
     - `trip_id`: Unique identifier for the trip.
     - `arrival_time`: Time of arrival at a stop.
     - `departure_time`: Time of departure from a stop.
     - `stop_id`: Unique identifier for the stop.
     - `stop_sequence`: Sequence order of stops.

5. `stops.csv`
   - Provides information about bus stops.
   - Columns:
     - `stop_id`: Unique identifier for the stop.
     - `stop_name`: Name of the stop.
     - `stop_lat`: Latitude of the stop location.
     - `stop_lon`: Longitude of the stop location.

6. `trips.csv`
   - Contains details about trips.
   - Columns:
     - `route_id`: Identifier of the route associated with the trip.
     - `trip_id`: Unique identifier for the trip.
     - `shape_id`: Identifier of the shape associated with the trip.

7. `line_freq.csv`
   - Contains data related to route frequency and geometry.
   - Columns:
     - `route_id`: Identifier of the route.
     - `route_name`: Name of the route.
     - `direction_id`: Identifier for the direction.
     - `window`: Time window for frequency data.
     - `min_per_trip`: Minimum minutes per trip.
     - `ntrips`: Number of trips.
     - `geometry`: Geometry data for visualization.

8. `segment_data.csv`
   - Provides information about route segments.
   - Columns:
     - `shape_id`: Identifier of the shape.
     - `route_id`: Identifier of the route.
     - `route_name`: Name of the route.
     - `direction_id`: Identifier for the direction.
     - `stop_sequence`: Sequence order of stops.
     - `segment_name`: Name of the segment.
     - `start_stop_name`: Name of the starting stop.
     - `end_stop_name`: Name of the ending stop.
     - `segment_id`: Unique identifier for the segment.
     - `start_stop_id`: Unique identifier for the starting stop.
     - `end_stop_id`: Unique identifier for the ending stop.
     - `distance_m`: Distance in meters.
     - `geometry`: Geometry data for visualization.

9. `speeds_data.csv`
   - Contains data related to bus speeds on route segments.
   - Columns:
     - `route_id`: Identifier of the route.
     - `route_name`: Name of the route.
     - `direction_id`: Identifier for the direction.
     - `stop_sequence`: Sequence order of stops.
     - `segment_name`: Name of the segment.
     - `window`: Time window for speed data.
     - `speed_kmh`: Speed in kilometers per hour.
     - `avg_route_speed_kmh`: Average route speed in kilometers per hour.
     - `segment_max_speed_kmh`: Maximum segment speed in kilometers per hour.
     - `runtime_sec`: Runtime in seconds.
     - `start_stop_name`: Name of the starting stop.
     - `end_stop_name`: Name of the ending stop.
     - `segment_id`: Unique identifier for the segment.
     - `start_stop_id`: Unique identifier for the starting stop.
     - `end_stop_id`: Unique identifier for the ending stop.
     - `shape_id`: Identifier of the shape.
     - `distance_m`: Distance in meters.
     - `geometry`: Geometry data for visualization.

10. `stop_freq.csv`
    - Contains data related to stop frequency.
    - Columns:
      - `stop_id`: Unique identifier for the stop.
      - `direction_id`: Identifier for the direction.
      - `window`: Time window for frequency data.
      - `ntrips`: Number of trips.
      - `min_per_trip`: Minimum minutes per trip.
      - `stop_name`: Name of the stop.
      - `geometry`: Geometry data for visualization.

## Data Usage

This dataset is intended for use in the Bus Congestion Prediction Project. It includes a variety of information about bus agencies, routes, shapes, stops, trips, and related attributes. The data can be used to analyze and model bus traffic congestion patterns, optimize routes, and make predictions related to bus service quality.

Please refer to the individual file descriptions for more details on the columns and their meanings. The data can be loaded into a data analysis or machine learning framework for further exploration and modeling.

## Licensing

Please note that the usage of this dataset may be subject to licensing agreements or restrictions, depending on the source of the data. Ensure that you comply with any applicable licensing terms and conditions when using this dataset.
