use gmanbus::utils::spawn_app;

// TODO: Add test case to ensure number of objects inside database
// is the same with the return objects
#[tokio::test]
async fn bus_lines_return_all_bus_lines() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/bus-lines", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

// TODO: Add query to the database first, then test against the api
#[tokio::test]
async fn get_bus_lines_by_id_return_valid_object() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!(
            "{}/bus-lines/100009",
            &address
        ))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
}

#[tokio::test]
async fn get_bus_lines_return_404_for_non_existed_id() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/bus-lines/12342", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert_eq!(404, response.status().as_u16());
}
