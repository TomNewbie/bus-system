use std::net::TcpListener;

use actix_cors::Cors;
use actix_web::{dev::Server, web::Data, App, HttpServer};
use mongodb::Client;
use tracing_actix_web::TracingLogger;

use crate::api::{
    bus_line::bus_line_config, bus_stop::bus_stop_config, health_check, predict::predict_config,
    segments::segments_config,
};

// TODO: Refactor the bus api after the get data
pub fn run(listener: TcpListener, client: Client) -> Result<Server, std::io::Error> {
    let client = Data::new(client);
    let server = HttpServer::new(move || {
        let cors = Cors::permissive();
        App::new()
            .wrap(TracingLogger::default())
            .wrap(cors)
            .service(health_check)
            .configure(bus_line_config)
            .configure(bus_stop_config)
            .configure(segments_config)
            .configure(predict_config)
            .app_data(client.clone())
    })
    .listen(listener)?
    .run();

    Ok(server)
}
