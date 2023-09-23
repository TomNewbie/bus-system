use gmanbus::{configuration, startup};
use mongodb::Client;
use std::net::TcpListener;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let configuration = configuration::get_configuration().expect("Failed to read configuration.");
    let address = format!("127.0.0.1:{}", configuration.application_port);

    let uri = configuration.database.connection_string();
    let client = Client::with_uri_str(uri)
        .await
        .expect("Failed to connect to MongoDB.");

    let listener = TcpListener::bind(address)?;
    startup::run(listener, client)?.await
}
