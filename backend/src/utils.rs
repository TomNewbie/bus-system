use std::net::TcpListener;

use mongodb::Client;
use secrecy::ExposeSecret;

use crate::{configuration, startup};

pub async fn spawn_app() -> String {
    let configuration = configuration::get_configuration().expect("Failed to read configuration.");
    let uri = configuration.database.connection_string();
    let uri = uri.expose_secret();
    let client = Client::with_uri_str(uri)
        .await
        .expect("Failed to connect to MongoDB.");
    let listener = TcpListener::bind("127.0.0.1:0").expect("Failed to bind random port");
    // We retrieve the port assigned to us by the OS
    let port = listener.local_addr().unwrap().port();
    let server = startup::run(listener, client).expect("Failed to bind address");
    tokio::spawn(server);
    // We return the application address to the caller!
    format!("http://127.0.0.1:{}", port)
}
