// TODO: Add test for bus stop

use std::vec;

use gmanbus::utils::spawn_app;

#[tokio::test]
async fn bus_stops_return_all_bus_stops() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/bus-stops", &address))
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
        .get(&format!("{}/bus-stops/1184", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

#[tokio::test]
async fn get_bus_stop_by_id_return_a_400_for_invalid_request() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();
    let test_cases = vec![("abcdef", "ID is not usize"), ("21430843", "ID not found")];

    for (invalid_body, error_msg) in test_cases {
        let response = client
            .get(&format!("{}/bus-stops/{}", &address, &invalid_body))
            .send()
            .await
            .expect("Failed to execute request");
        assert_eq!(
            400,
            response.status().as_u16(),
            "The API did not fail with 400 Bad Request when the payload was {}.",
            error_msg
        )
    }
}
