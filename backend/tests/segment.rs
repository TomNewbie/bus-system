use gmanbus::utils::spawn_app;

#[tokio::test]
async fn segments_return_ok() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/de/segments", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}
