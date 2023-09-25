use actix_web::{
    get,
    web::{self, Data, Path, ServiceConfig},
    HttpResponse, routes,
};
use bson::oid::ObjectId;
use mongodb::Client;

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
async fn get_all_bus_lines(_db: Data<Client>) -> HttpResponse {
    // TODO: add query to mongodb, mock objects from database for now.
    let bus_lines = vec![
        BusLine {
            id: Some(ObjectId::new()),
            name: "sth".to_owned(),
            start_dest: "VN".to_owned(),
            end_dest: "Finland".to_owned(),
            duration: 69.69,
        },
        BusLine {
            id: Some(ObjectId::new()),
            name: "sth".to_owned(),
            start_dest: "VN".to_owned(),
            end_dest: "Finland".to_owned(),
            duration: 69.69,
        },
        BusLine {
            id: Some(ObjectId::new()),
            name: "sth".to_owned(),
            start_dest: "VN".to_owned(),
            end_dest: "Finland".to_owned(),
            duration: 69.69,
        },
    ];

    HttpResponse::Ok().json(bus_lines)
}

// TODO: Add database query
#[get("/{id}")]
async fn get_bus_line_by_id(_db: Data<Client>, _path: Path<String>) -> HttpResponse {
    // Sample data for now for the purpose of testing
    let id = r#"
  {
    "$oid": "651137007b4ebbc415c07d0c"
  },
  "#;
    let id = ObjectId::parse_str(&id).ok();
    let obj = BusLine {
        id,
        name: "sth".to_owned(),
        start_dest: "VN".to_owned(),
        end_dest: "Finland".to_owned(),
        duration: 69.69,
    };

    HttpResponse::Ok().json(obj)
}
