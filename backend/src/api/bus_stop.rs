use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse,
};
use bson::{doc, Bson};
use futures::TryStreamExt;
use mongodb::{Client, Collection};

use crate::models::bus_stop::{BusStopWithoutTrip, BusStopWithTrip};

pub fn bus_stop_config(cfg: &mut ServiceConfig) {
    cfg.service(
        web::scope("/bus-stops")
            .service(get_all_bus_stops)
            .service(get_bus_stop_by_id),
    );
}

#[routes]
#[get("")]
#[get("/")]
async fn get_all_bus_stops(db_client: Data<Client>) -> HttpResponse {
    let col: Collection<BusStopWithoutTrip> = db_client.database("sampledb").collection("stops");
    let cursor = match col.find(doc! {}, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let bus_stops: Vec<BusStopWithoutTrip> = match cursor.try_collect().await {
        Ok(stops) => stops,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(bus_stops)
}

#[get("/{id}")]
async fn get_bus_stop_by_id(db_client: Data<Client>, path: Path<String>) -> HttpResponse {
    let id = path.into_inner();

    if id.is_empty() {
        return HttpResponse::BadRequest().body("invalid ID");
    }

    let id: usize = match id.parse() {
        Ok(id) => id,
        Err(err) => {
            tracing::error!("Failed to parse the ID: {:?}", err);
            return HttpResponse::BadRequest().body("invalid ID");
        }
    };

    let col: Collection<BusStopWithTrip> = db_client.database("sampledb").collection("stops");
    let filter = doc! {"stop_id": Bson::Int64(id as i64)};
    let bus_stop = match col.find_one(filter, None).await {
        Ok(opt) => match opt {
            Some(bus_stop) => bus_stop,
            None => {
                tracing::error!("stop_id: {} not found", id);
                return HttpResponse::NotFound().body("ID not found");
            }
        },
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(bus_stop)
}
