use std::net::TcpListener;

use actix_web::{dev::Server, web::Data, App, HttpServer};
use mongodb::Client;
use tracing_actix_web::TracingLogger;

use crate::api::{
    bus_line::bus_line_config,
    health_check, sample,
};

// TODO: Refactor the bus api after the get data
pub fn run(listener: TcpListener, client: Client) -> Result<Server, std::io::Error> {
    let client = Data::new(client);
    let server = HttpServer::new(move || {
        App::new()
            .wrap(TracingLogger::default())
            .service(health_check)
            .service(sample)
            .configure(bus_line_config)
            .app_data(client.clone())
    })
    .listen(listener)?
    .run();

    Ok(server)
}
