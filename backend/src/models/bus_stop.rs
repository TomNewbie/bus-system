use bson::oid::ObjectId;
use serde::{Deserialize, Serialize};

// TODO: add join on bus stop
#[derive(Debug, Serialize, Deserialize, PartialEq)]
pub struct BusStop {
    #[serde(rename = "_id", skip_serializing_if = "Option::is_none")]
    pub id: Option<ObjectId>,
    pub name: String,
}
