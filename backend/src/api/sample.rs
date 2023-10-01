use actix_web::{get, web, HttpResponse, Responder};
use bson::{doc, oid::ObjectId, Bson, DateTime};
use futures::stream::TryStreamExt;
use mongodb::{Client, Collection};
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "PascalCase")]
pub struct SampleData {
    #[serde(rename = "_id")]
    id: ObjectId,
    vehicle_number: String,
    is_l_l_valid: bool,
    loc: Vec<f64>,
    hdg_deg: f64,
    speed: f64,
    last_rec_rcvd_d_t_s: DateTime,
    service_date: DateTime,
    current_trip_id: ObjectId,
    current_route_var_id: usize,
    current_timepoint_id: usize,
    current_geo_path_id: usize,
    current_stop_id: usize,
    next_stop_id: usize,
    trip_id: usize,
    trip_type_id: usize,
    trip_start_d_t_s: DateTime,
    last_time_point: usize,
    next_time_point: usize,
    is_in_depot: bool,
    depot_out_d_t_s: DateTime,
    depot_in_d_t_s: DateTime,
    depot_i_d_last_out: usize,
    depot_i_d_last_in: usize,
    employee_id: usize,
    add_d_t_s: DateTime,
    upd_d_t_s: DateTime,
    location_update_d_t_s: DateTime,
    next_trip_id: usize,
    is_in_timepoint: bool,
    timepoint_out_d_t_s: DateTime,
    timepoint_in_d_t_s: DateTime,
    timepoint_i_d_last_out: usize,
    timepoint_i_d_last_in: usize,
    work_status_id: usize,
    route_id: usize,
    raw_log_id: ObjectId,
    statuses: Bson,
    events: Bson,
    distance_into_trip: Bson,
    total_trips: usize,
    version_id: usize,
    event_detector_flags: Bson,
    path_order: usize,
    distance_to_path: usize,
    drv_permit: String,
    drv_name: String,
    flag: Bson,
    rou_id: Bson,
}

// TODO: add error handling
#[get("/sample")]
#[tracing::instrument(name = "Getting sample data", skip(client))]
pub async fn sample(client: web::Data<Client>) -> impl Responder {
    let coll: Collection<SampleData> = client.database("sampledb").collection("sample");
    let docs = coll.find(doc! {}, None).await.unwrap();
    let res = docs.try_collect::<Vec<SampleData>>().await.unwrap();
    HttpResponse::Ok().json(res)
}
