use gmanbus::{api::SampleData, utils::spawn_app};

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
