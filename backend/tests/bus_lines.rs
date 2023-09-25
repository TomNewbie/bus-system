use bson::oid::ObjectId;
use gmanbus::{models::bus_line::BusLine, utils::spawn_app};

const NBUSLINES: usize = 3;

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
    let objs = response.json::<Vec<BusLine>>().await.unwrap();
    assert_eq!(objs.len(), NBUSLINES);
}

// TODO: Add query to the database first, then test against the api
#[tokio::test]
async fn get_bus_lines_by_id_return_valid_object() {
    let id = r#"
  {
    "$oid": "651137007b4ebbc415c07d0c"
  },
  "#;
    let id = ObjectId::parse_str(&id).ok();
    let obj = BusLine {
        id,
        name: "sth".to_owned(),
        start_dest: "VN".to_owned(),
        end_dest: "Finland".to_owned(),
        duration: 69.69,
    };

    let address = spawn_app().await;
    let client = reqwest::Client::new();

    let response = client
        .get(&format!("{}/bus-lines/651137007b4ebbc415c07d0c", &address))
        .send()
        .await
        .expect("Failed to execute request");

    assert!(response.status().is_success());
    let ret_obj = response.json::<BusLine>().await.unwrap();
    assert_eq!(obj, ret_obj);
}
