use bson::Document;
use gmanbus::utils::spawn_app;

// TODO: Add test case to ensure number of objects inside database
// is the same with the return objects
#[tokio::test]
async fn segments_return_200_first_segments() {
    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/segments", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
    let payload = response.json::<Vec<Document>>().await.unwrap();
    assert_eq!(payload.len(), 200);
}
