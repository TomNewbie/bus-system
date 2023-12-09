use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct RouteInfo {
    pub trip_id: String,
    pub start_stop_id: String,
    pub arrival_time: String,
    pub arrival_hour: i64,
    pub arrival_minute: i64,
    pub stop_sequence_x: i64,
    pub stop_lat: f64,
    pub stop_lon: f64,
    pub route_id: String,
    pub direction_id: f64,
    pub next_lat: f64,
    pub next_lon: f64,
    pub congestion_level: i64,
    pub end_stop_id: String,
    pub runtime_sec: f64,
}
