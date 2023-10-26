use gmanbus::utils::spawn_app;

#[tokio::test]
async fn dummy_predict_works() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .post(&format!("{}/predict/dummy", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}
