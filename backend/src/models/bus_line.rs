use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusLineWithoutStop {
    pub route_id: String,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub agency_name: String,
}
#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusLineWithStop {
    pub route_id: String,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub agency_name: String,
    pub stops: Vec<BusStop>,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStop {
    pub stop_id: String,
    pub stop_sequence: usize,
    pub stop_name: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
}
