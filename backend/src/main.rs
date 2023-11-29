use gmanbus::{
    configuration, startup,
    telemetry::{get_subscriber, init_subscriber},
};
use mongodb::Client;
use secrecy::ExposeSecret;
use std::net::TcpListener;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let subscriber = get_subscriber("gmanbus".into(), "info".into());
    init_subscriber(subscriber);

    let configuration = configuration::get_configuration().expect("Failed to read configuration.");
    let address = format!(
        "{}:{}",
        configuration.application.host, configuration.application.port
    );

    let uri = configuration.database.connection_string();
    let uri = uri.expose_secret();
    let client = Client::with_uri_str(uri)
        .await
        .expect("Failed to connect to MongoDB.");

    let listener = TcpListener::bind(address)?;
    startup::run(listener, client)?.await
}
