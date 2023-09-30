use bson::oid::ObjectId;
use serde::{Deserialize, Serialize};

// TODO: add join on bus stop
#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusLine {
    pub route_id: usize,
    pub trip_id: String,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub agency_name: String,
}
