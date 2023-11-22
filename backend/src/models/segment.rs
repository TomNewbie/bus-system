use bson::oid::ObjectId;
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, PartialEq, Clone)]
pub struct Segment {
    pub _id: ObjectId,
    #[serde(rename = "type")]
    pub _type: String,
    pub properties: Properties,
    pub geometry: Geometry,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Clone)]
pub struct Properties {
    pub shape_id: String,
    pub route_id: String,
    pub route_name: String,
    pub direction_id: i64,
    pub stop_sequence: i64,
    pub segment_name: String,
    pub start_stop_name: String,
    pub end_stop_name: String,
    pub segment_id: String,
    pub start_stop_id: String,
    pub end_stop_id: String,
    pub distance_m: f64,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Clone)]
pub struct Geometry {
    #[serde(rename = "type")]
    pub _type: String,
    pub coordinates: Vec<[f64; 2]>,
}

#[derive(Debug, Serialize, Deserialize, PartialEq, Clone)]
pub struct SegmentWithCongestionLevel {
    pub _id: ObjectId,
    #[serde(rename = "type")]
    pub _type: String,
    pub properties: Properties,
    pub geometry: Geometry,
    pub congestion_level: i64,
}
