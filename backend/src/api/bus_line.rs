use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse,
};
use bson::doc;
use futures::TryStreamExt;
use mongodb::{Client, Collection};

use crate::models::{BusLineWithStop, BusLineWithoutStop};

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
    let col: Collection<BusLineWithoutStop> = db_client.database("sampledb").collection("lines");
    let cursor = match col.find(doc! {}, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let bus_lines: Vec<BusLineWithoutStop> = match cursor.try_collect().await {
        Ok(lines) => lines,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(bus_lines)
}

#[get("/{id}")]
async fn get_bus_line_by_id(db_client: Data<Client>, path: Path<String>) -> HttpResponse {
    let id = path.into_inner();

    if id.is_empty() {
        return HttpResponse::BadRequest().body("invalid ID");
    }

    let col: Collection<BusLineWithStop> = db_client.database("sampledb").collection("lines");
    let filter = doc! {"trip_id": &id};
    let bus_line = match col.find_one(filter, None).await {
        Ok(opt) => match opt {
            Some(bus_line) => bus_line,
            None => {
                tracing::error!("trip_id: {} not found", id);
                return HttpResponse::NotFound().body("ID not found");
            }
        },
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(bus_line)
}
