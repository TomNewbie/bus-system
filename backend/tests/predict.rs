use gmanbus::utils::spawn_app;
use serde::{Deserialize, Serialize};

const QUERY: &'static str = "?route_id=100007&shape_id=2358&direction_id=1&minute_predict=120";
#[tokio::test]
async fn lstm_prediction_ok() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();
    let query = format!("{}{}", "lstm", QUERY);

    let response = client
        .get(&format!("{}/de/predict/{}", &address, query))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

#[tokio::test]
async fn random_forest_prediction_ok() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();
    let query = format!("{}{}", "random-forest", QUERY);

    let response = client
        .get(&format!("{}/de/predict/{}", &address, query))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

#[derive(Debug, Clone, Serialize, Deserialize)]
struct ResposneError {
    error: String,
}

#[tokio::test]
async fn unsupported_model_not_found() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();
    let query = format!("{}{}", "trash", QUERY);

    let response = client
        .get(&format!("{}/de/predict/{}", &address, query))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().as_u16() == 404);
    let response = response.json::<ResposneError>().await.unwrap();
    assert_eq!(response.error.as_str(), "Model trash not supported")
}
