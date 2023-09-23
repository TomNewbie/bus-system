use std::net::TcpListener;

use gmanbus::{api::SampleData, configuration};
use mongodb::Client;

#[tokio::test]
async fn health_check_works() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/health_check", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
    assert_eq!(Some(0), response.content_length());
}

#[tokio::test]
async fn sample_returns_100_json_objects() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/sample", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
    let objs = response.json::<Vec<SampleData>>().await.unwrap();
    assert_eq!(objs.len(), 100);
}

async fn spawn_app() -> String {
    let configuration = configuration::get_configuration().expect("Failed to read configuration.");
    let uri = configuration.database.connection_string();
    let client = Client::with_uri_str(uri)
        .await
        .expect("Failed to connect to MongoDB.");
    let listener = TcpListener::bind("127.0.0.1:0").expect("Failed to bind random port");
    // We retrieve the port assigned to us by the OS
    let port = listener.local_addr().unwrap().port();
    let server = gmanbus::startup::run(listener, client).expect("Failed to bind address");
    let _ = tokio::spawn(server);
    // We return the application address to the caller!
    format!("http://127.0.0.1:{}", port)
}
