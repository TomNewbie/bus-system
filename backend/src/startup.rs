use std::net::TcpListener;

use actix_web::{dev::Server, web::Data, App, HttpServer};
use mongodb::Client;

use crate::api::{health_check, sample};

pub fn run(listener: TcpListener, client: Client) -> Result<Server, std::io::Error> {
    let client = Data::new(client);
    let server = HttpServer::new(move || {
        App::new()
            .service(health_check)
            .service(sample)
            .app_data(client.clone())
    })
    .listen(listener)?
    .run();

    Ok(server)
}
