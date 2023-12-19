use gmanbus::utils::spawn_app;

#[tokio::test]
async fn bus_stops_return_all_bus_stops() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/de/bus-stops", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

// TODO: Add query to the database first, then test against the api
#[tokio::test]
async fn get_bus_stop_by_id_return_valid_object() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/de/bus-stops/1184", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}
