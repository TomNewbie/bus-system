use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpRequest, HttpResponse,
};
use bson::{doc, Document};
use futures::TryStreamExt;
use mongodb::{Client, Collection};

use crate::{models::BusLineWithoutStop, utils::country_to_db_name};

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
async fn get_all_bus_lines(req: HttpRequest, db_client: Data<Client>) -> HttpResponse {
    let country = req.match_info().get("country").unwrap();
    let db_name = match country_to_db_name(&country) {
        Some(name) => name,
        None => {
            return HttpResponse::NotFound().finish();
        }
    };
    let col: Collection<BusLineWithoutStop> = db_client.database(&db_name).collection("lines");
    let cursor = match col.find(doc! {}, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the queryab: {:?}", err);
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
async fn get_bus_line_by_id(db_client: Data<Client>, path: Path<(String, String)>) -> HttpResponse {
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

    let col: Collection<Document> = db_client.database(&db_name).collection("segments");
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
