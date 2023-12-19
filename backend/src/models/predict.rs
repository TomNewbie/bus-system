use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct PredictionSegment {
    pub segment_id: String,
    pub start_stop_id: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
    pub end_stop_id: String,
    pub next_lat: f64,
    pub next_lon: f64,
    pub runtime_sec: f64,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct PredictionRoute {
    pub route_id: String,
    pub direction_id: i64,
    pub arrival_hour: u32,
    pub arrival_minute: u32,
    pub segments: Vec<PredictionSegment>,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct PredictedRouteInfo {
    pub start_stop_id: String,
    pub arrival_hour: i64,
    pub arrival_minute: i64,
    pub end_stop_id: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
    pub route_id: String,
    pub direction_id: i64,
    pub segment_id: String,
    pub next_lat: f64,
    pub next_lon: f64,
    pub congestion_level: i64,
}
