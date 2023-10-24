import pandas as pd

trips = pd.read_csv("trips.csv")
segments = pd.read_csv("segment_data.csv")
agency = pd.read_csv("agency.csv")
routes = pd.read_csv("routes.csv")


columns_segments = ['shape_id', 'route_id', 'start_stop_name', 'end_stop_name']

merged = trips.merge(segments[columns_segments], on=['shape_id', 'route_id'], how='left')

routes_agency = routes.merge(agency, on='agency_id', how='left')

final_df = merged.merge(routes_agency[['route_id', 'agency_name']], on='route_id', how='left')

final_df.to_csv('trips.csv', index=False)