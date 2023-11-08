use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse,
};
use bson::{doc, Document};
use futures::TryStreamExt;
use mongodb::{Client, Collection};

use crate::models::BusLineWithoutStop;

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
    let col: Collection<BusLineWithoutStop> = db_client.database("bus").collection("lines");
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

    let col: Collection<Document> = db_client.database("bus").collection("segments");
    let filter = doc! {"properties.route_id": id.clone()};
    let cursor = match col.find(filter, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let lines: Vec<Document> = match cursor.try_collect().await {
        Ok(lines) => lines,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    if lines.is_empty() {
        tracing::error!("route_id: {} not found", id);
        return HttpResponse::NotFound().body("ID not found");
    }

    HttpResponse::Ok().json(lines)
}
