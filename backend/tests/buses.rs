// TODO: Add test for bus stop

use gmanbus::utils::spawn_app;

// TODO: Add test case to ensure number of objects inside database
// is the same with the return objects
#[tokio::test]
async fn buses_return_all_bus_stops_and_bus_lines() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/buses", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

// TODO: Add query to the database first, then test against the api
// Add more exotic test case
#[tokio::test]
async fn search_bus_by_name_return_valid_object() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/buses?name=", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}
