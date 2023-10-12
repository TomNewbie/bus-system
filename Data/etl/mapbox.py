import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

stops = pd.read_csv("stops.csv")
stop_times = pd.read_csv("stop_times.csv")
trips = pd.read_csv("trips.csv")
shapes = pd.read_csv("shapes.csv")


stops1000 = stops.head(1000)
stops1000_merged = stops1000.merge(stop_times[['stop_id', 'trip_id']].drop_duplicates(subset=['stop_id']), on='stop_id', how='inner')

shape10 = shapes[(shapes['shape_id'] >= 0) & (shapes['shape_id'] <= 300)]

# Create a scatter map using Mapbox
fig = go.Figure()
fig.add_trace(go.Scattermapbox(
    lat=stops1000['stop_lat'],
    lon=stops1000['stop_lon'],
    mode='markers+text',
    marker=dict(size=40, color='blue'),
    textposition='bottom center'
))
"""fig.add_trace(go.Scattermapbox(
        lat=shape10['shape_pt_lat'],
        lon=shape10['shape_pt_lon'],
        mode='lines',
        line=dict(color='red', width=3),
    ))"""

for shape_id in shape10['shape_id'].unique():
    shape_points = shape10[shape10['shape_id'] == shape_id]
    trace = go.Scattermapbox(
        lat=shape_points['shape_pt_lat'],
        lon=shape_points['shape_pt_lon'],
        mode='lines',
        line=dict(color='red', width=3),
        name=f'Shape {shape_id}',
    )
    fig.add_trace(trace)
fig.update_traces(
    marker=dict(
        size=8,
        opacity=0.8
    ),
)
# Set the Mapbox access token (replace 'YOUR_MAPBOX_ACCESS_TOKEN' with your actual token)
fig.update_layout(
    mapbox=dict(
        accesstoken='pk.eyJ1IjoibWluaHZ0MCIsImEiOiJjbG43aHo0OTMwZ3U0MnFwOWc2YWRyaXlmIn0.H6OTMKveXJU1_7lf68eQOA',
        style='mapbox://styles/mapbox/navigation-night-v1',  # Mapbox style
    )
)
fig.update_layout(
    mapbox_center={"lat": stops1000['stop_lat'].mean(), "lon": stops1000['stop_lon'].mean()}  # Set the center of the map
)
# Show the map
fig.show()