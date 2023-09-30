use serde::{Deserialize, Serialize};
#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStopWithoutTrip {
    pub stop_id: usize,
    pub stop_name: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStopWithTrip {
    pub stop_id: usize,
    pub stop_name: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
    pub trips: Vec<BusTrip>,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusTrip {
    pub trip_id: String,
    pub route_id: usize,
    pub shape_id: usize,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub agency_name: String,
}