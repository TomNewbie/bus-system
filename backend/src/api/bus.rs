use actix_web::{
    get, routes,
    web::{self, Data, Query, ServiceConfig},
    HttpResponse,
};
use mongodb::Client;
use serde::{Deserialize, Serialize};

pub fn bus_config(cfg: &mut ServiceConfig) {
    cfg.service(
        web::scope("/buses")
            .service(get_all_bus_stops_and_bus_line)
            .service(search_by_name),
    );
}

#[routes]
#[get("")]
#[get("/")]
async fn get_all_bus_stops_and_bus_line(_db: Data<Client>) -> HttpResponse {
    // TODO: Add implementation when the data comes
    HttpResponse::Ok().finish()
}

#[derive(Debug, Serialize, Deserialize)]
struct Name {
    name: String,
}

#[get("/")]
async fn search_by_name(_db: Data<Client>, _query: Query<Name>) -> HttpResponse {
    // TODO: Add implementation when the data comes
    HttpResponse::Ok().finish()
}
