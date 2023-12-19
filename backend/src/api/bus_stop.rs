use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpRequest, HttpResponse,
};
use bson::doc;
use futures::TryStreamExt;
use mongodb::{Client, Collection};

use crate::{
    models::bus_stop::{BusStopWithTrip, BusStopWithoutTrip},
    utils::country_to_db_name,
};

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
async fn get_all_bus_stops(req: HttpRequest, db_client: Data<Client>) -> HttpResponse {
    let country = req.match_info().get("country").unwrap();
    let db_name = match country_to_db_name(&country) {
        Some(name) => name,
        None => {
            return HttpResponse::NotFound().finish();
        }
    };
    let col: Collection<BusStopWithoutTrip> = db_client.database(&db_name).collection("stops");
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
async fn get_bus_stop_by_id(db_client: Data<Client>, path: Path<(String, String)>) -> HttpResponse {
    let (country, id) = path.into_inner();

    if id.is_empty() || country.is_empty() {
        return HttpResponse::BadRequest().body("invalid ID");
    }

    let db_name = match country_to_db_name(&country) {
        Some(name) => name,
        None => {
            return HttpResponse::NotFound().finish();
        }
    };

    let col: Collection<BusStopWithTrip> = db_client.database(&db_name).collection("stops");
    let filter = doc! {"stop_id": id.clone()};
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
