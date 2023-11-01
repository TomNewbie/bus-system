use actix_web::{
    get, post,
    web::{self, Data, Query, ServiceConfig},
    HttpResponse,
};
use bson::{doc, Bson, Document};
use chrono::{Duration, Timelike, Utc};
use futures::TryStreamExt;
use lazy_static::lazy_static;
use mongodb::{error::Error, Client, Collection};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use tokio::try_join;

use crate::models::{route_info::RouteInfo, Segment};

lazy_static! {
    static ref URL: &'static str = std::env::var("APP_ENVIRONMENT")
        .map(|_| "tfserving")
        .unwrap_or("localhost");
}

pub fn predict_config(cfg: &mut ServiceConfig) {
    cfg.service(
        web::scope("/predict")
            .service(dummy_predict)
            .service(predict_congestion),
    );
}

#[derive(Debug, Deserialize)]
pub struct SegmentInfo {
    route_id: String,
    shape_id: String,
    direction_id: i64,
}

async fn fetch_segments(
    db_client: &Data<Client>,
    shape_id: &String,
    route_id: &String,
    direction_id: i64,
) -> Result<Vec<Segment>, Error> {
    let col: Collection<Document> = db_client.database("bus").collection("segments");
    let filter = doc! {
        "properties.shape_id": shape_id,
        "properties.route_id": route_id,
        "properties.direction_id": Bson::Int64(direction_id),
    };
    let mut cursor = col.find(filter, None).await?;
    let mut segments: Vec<Segment> = Vec::new();
    while let Some(doc) = cursor.try_next().await? {
        let segment = bson::from_document(doc)?;
        segments.push(segment);
    }
    segments.sort_unstable_by_key(|k| k.properties.stop_sequence);
    Ok(segments)
}

async fn fetch_route_info(
    db_client: &Data<Client>,
    route_id: i64,
    direction_id: i64,
) -> Result<Vec<RouteInfo>, Error> {
    let col: Collection<Document> = db_client.database("bus").collection("route_info");
    let filter = doc! {
        "route_id": Bson::Int64(route_id),
        "direction_id": Bson::Int64(direction_id),
    };
    let mut cursor = col.find(filter, None).await?;
    let mut routes: Vec<RouteInfo> = Vec::new();
    while let Some(doc) = cursor.try_next().await? {
        let route = bson::from_document(doc)?;
        routes.push(route);
    }
    routes.sort_unstable_by_key(|k| k.stop_sequence_x);
    Ok(routes)
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct PredictionSegment {
    segment_id: String,
    start_stop_id: i64,
    stop_lat: f64,
    stop_lon: f64,
    end_stop_id: i64,
    next_lat: f64,
    next_lon: f64,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct PredictionRoute {
    route_id: i64,
    direction_id: i64,
    arrival_hour: u32,
    arrival_minute: u32,
    segments: Vec<PredictionSegment>,
}

#[get("")]
pub async fn predict_congestion(
    db_client: Data<Client>,
    segment_info: Query<SegmentInfo>,
) -> HttpResponse {
    let time_for_prediction = (Utc::now() + Duration::minutes(10)).time();
    let SegmentInfo {
        route_id,
        shape_id,
        direction_id,
    } = segment_info.into_inner();
    tracing::info!("Request Info: Id of route - {route_id}, Id of shape - {shape_id}");

    let route_id_i64 = match route_id.parse::<i64>() {
        Ok(route_id) => route_id,
        Err(err) => {
            tracing::error!("Failed to execute parsing number: {}", err);
            return HttpResponse::BadRequest().finish();
        }
    };
    let routes = fetch_route_info(&db_client, route_id_i64, direction_id);
    let segments = fetch_segments(&db_client, &shape_id, &route_id, direction_id);
    let joined_stream = try_join!(routes, segments);
    let (routes, segments) = match joined_stream {
        Ok(joined_output) => joined_output,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    tracing::info!("Len of segments: {}", segments.len());
    tracing::info!("Len of routes: {}", routes.len());
    let prediction_segments = routes
        .iter()
        .zip(segments.iter())
        .map(|(route, segment)| PredictionSegment {
            segment_id: segment.properties.segment_id.clone(),
            start_stop_id: route.start_stop_id,
            stop_lat: route.stop_lat,
            stop_lon: route.stop_lon,
            end_stop_id: route.start_stop_id,
            next_lat: route.next_lat,
            next_lon: route.next_lon,
        })
        .collect::<Vec<_>>();
    let prediction_route = PredictionRoute {
        segments: prediction_segments,
        route_id: route_id_i64,
        direction_id,
        arrival_hour: time_for_prediction.hour(),
        arrival_minute: time_for_prediction.minute(),
    };
    HttpResponse::Ok().json(prediction_route)
}

// Dummy route to test for connection to tensorflow serving for model deployment
#[post("dummy")]
pub async fn dummy_predict() -> HttpResponse {
    let url = format!("http://{}:8501/v1/models/lstm:predict", URL.clone());
    let client = reqwest::Client::new();
    let body = r#"
      {
      "instances": [[[ 6.454545e-01,  2.03389831e-01, -5.20189830e+01, -1.05500952e+00,
        -5.20837128e+01, -1.07696162e+00,  4.482300000e-02,  4.54339964e-02,
         9.41837409e-01,  0.00000000e+00,  0.00000000e+00]]]
      }
    "#;
    let body: Value = match serde_json::from_str(body) {
        Ok(body) => body,
        Err(err) => {
            tracing::error!("Unable to deserialize json object: {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let resp = client.post(url).json(&body).send().await;
    let resp = match resp {
        Ok(resp) => resp,
        Err(err) => {
            tracing::error!("Error sending prediction request {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    let status = resp.status();
    let resp: Document = match resp.json().await {
        Ok(resp) => resp,
        Err(err) => {
            tracing::error!("Error sending prediction request {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    if !status.is_success() {
        tracing::error!("Error sending prediction request {}", resp);
        return HttpResponse::InternalServerError().finish();
    }
    HttpResponse::Ok().json(resp)
}
