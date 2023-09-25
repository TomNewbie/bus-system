use actix_web::{
    get, routes,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse,
};
use mongodb::Client;

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
async fn get_all_bus_stops(_db: Data<Client>) -> HttpResponse {
    // TODO: Add implementation when the data comes
    HttpResponse::Ok().finish()
}

#[get("/{id}")]
// TODO: Add implementation when the data comes
async fn get_bus_stop_by_id(_db: Data<Client>, _path: Path<String>) -> HttpResponse {
    HttpResponse::Ok().finish()
}
