use serde::{Deserialize, Serialize};
#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStopWithoutTrip {
    pub stop_id: String,
    pub stop_name: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStopWithTrip {
    pub stop_id: String,
    pub stop_name: String,
    pub stop_lat: f64,
    pub stop_lon: f64,
    pub routes: Vec<BusRoute>,
}

#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusRoute {
    pub route_id: String,
    pub shape_id: String,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub agency_name: String,
}
