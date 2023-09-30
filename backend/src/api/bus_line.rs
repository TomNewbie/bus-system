use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse,
};
use bson::{doc, oid::ObjectId};
use futures::{TryFutureExt, TryStreamExt};
use mongodb::{Client, Collection};

use crate::models::BusLine;

pub fn bus_line_config(cfg: &mut ServiceConfig) {
    cfg.service(
        web::scope("/bus-lines")
            .service(get_all_bus_lines)
            .service(get_bus_line_by_id),
    );
}

#[routes]
#[get("")]
#[get("/")]
async fn get_all_bus_lines(db_client: Data<Client>) -> HttpResponse {
    // TODO: add query to mongodb, mock objects from database for now.
    // TODO: add error handling
    let col: Collection<BusLine> = db_client.database("sampledb").collection("trips");
    let stage_limit = doc! { "$limit": 100};
    let pipeline = vec![stage_limit];
    let mut bus_lines: Vec<BusLine> = Vec::new();
    let mut cursor = col.aggregate(pipeline, None).await.unwrap();
    while let Some(line) = cursor.try_next().await.unwrap() {
        let line = bson::from_document(line).unwrap();
        bus_lines.push(line);
    }

    HttpResponse::Ok().json(bus_lines)
}

// TODO: Add database query
// TODO: Add error handling
#[get("/{id}")]
async fn get_bus_line_by_id(db_client: Data<Client>, path: Path<String>) -> HttpResponse {
    let id = path.into_inner();
    
    if id.is_empty() {
        return HttpResponse::BadRequest().body("invalid ID");
    }

    let col: Collection<BusLine> = db_client.database("sampledb").collection("trips");
    let stage_match_trip_id = doc! {
        "$match": { "trip_id" : id },
    };

    let stage_limit_1 = doc! {
        "$limit": 1
    };

    let stage_lookup_stop_times = doc! {
        "$lookup": {
            "from": "stop_times",
            "localField": "trip_id",
            "foreignField": "trip_id",
            "as": "stop_time"
        }
    };

    let stage_unwind = doc! {
        "$unwind": "$stop_time"
    };

    let pipeline = vec![stage_match_trip_id, stage_limit_1, stage_lookup_stop_times, stage_unwind];
    let mut cursor = col.aggregate(pipeline, None).await.unwrap();
    let doc = cursor.try_next().await.unwrap().unwrap();
    println!("{:?}", doc);    

    HttpResponse::BadRequest().finish()
}
