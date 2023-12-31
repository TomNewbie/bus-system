use actix_web::{
    get,
    web::{self, Data, Query, ServiceConfig},
    HttpRequest, HttpResponse,
};
use bson::{doc, Bson, Document};
use chrono::{Duration, Timelike, Utc};
use futures::TryStreamExt;
use lazy_static::lazy_static;
use mongodb::{error::Error, Client, Collection, Database};
use serde::{Deserialize, Serialize};
use serde_json::json;
use tokio::try_join;

use crate::{
    models::{
        route_info::RouteInfo, PredictedRouteInfo, PredictionRoute, PredictionSegment, Segment,
        SegmentWithCongestionLevel,
    },
    utils::country_to_db_name,
};

lazy_static! {
    static ref URL: &'static str = std::env::var("APP_ENVIRONMENT")
        .map(|_| "157.245.204.41")
        .unwrap_or("localhost");
}

pub fn predict_config(cfg: &mut ServiceConfig) {
    cfg.service(web::scope("/predict").service(predict_congestion));
}

#[derive(Debug, Serialize, Deserialize)]
pub struct SegmentInfo {
    route_id: String,
    shape_id: String,
    direction_id: i64,
    minute_predict: i64,
}

async fn fetch_segments(
    db: &Database,
    shape_id: &String,
    route_id: &String,
    direction_id: i64,
) -> Result<Vec<Segment>, Error> {
    let col: Collection<Document> = db.collection("segments");
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
    db: &Database,
    route_id: String,
    direction_id: i64,
) -> Result<Vec<RouteInfo>, Error> {
    let col: Collection<Document> = db.collection("route_info");
    let filter = doc! {
        "route_id": route_id.clone(),
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

#[get("/{model}")]
pub async fn predict_congestion(
    req: HttpRequest,
    db_client: Data<Client>,
    segment_info: Query<SegmentInfo>,
) -> HttpResponse {
    let country = req.match_info().get("country").unwrap();
    let db_name = match country_to_db_name(&country) {
        Some(name) => name,
        None => {
            return HttpResponse::NotFound().finish();
        }
    };
    let model: String = match req.match_info().get("model") {
        None => return HttpResponse::BadRequest().finish(),
        Some(model) => match model {
            "lstm" | "random-forest" => {
                if country == "ca" {
                    String::from(model) + "-2"
                } else {
                    model.to_string()
                }
            },
            path => {
                let msg = format!("Model {} not supported", path);
                tracing::error!(msg);
                let resp = json!({
                    "error": msg,
                });
                return HttpResponse::NotFound().json(resp);
            }
        },
    };

    let db = db_client.database(&db_name);
    let SegmentInfo {
        route_id,
        shape_id,
        direction_id,
        minute_predict,
    } = segment_info.into_inner();
    let time_for_prediction = (Utc::now() + Duration::minutes(minute_predict)).time();

    let routes = fetch_route_info(&db, route_id.clone(), direction_id);
    let segments = fetch_segments(&db, &shape_id, &route_id, direction_id);
    let joined_stream = try_join!(routes, segments);
    let (routes, segments) = match joined_stream {
        Ok(joined_output) => joined_output,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let prediction_segments = routes
        .iter()
        .zip(segments.iter())
        .map(|(route, segment)| PredictionSegment {
            segment_id: segment.properties.segment_id.clone(),
            start_stop_id: route.start_stop_id.clone(),
            stop_lat: route.stop_lat,
            stop_lon: route.stop_lon,
            end_stop_id: route.end_stop_id.clone(),
            next_lat: route.next_lat,
            next_lon: route.next_lon,
            runtime_sec: route.runtime_sec,
        })
        .collect::<Vec<_>>();
    let prediction_route = PredictionRoute {
        segments: prediction_segments,
        route_id: route_id.clone(),
        direction_id,
        arrival_hour: time_for_prediction.hour(),
        arrival_minute: time_for_prediction.minute(),
    };
    let url = format!("http://{}:5000/{}", URL.clone() , model);
    let client = reqwest::Client::new();
    let resp = match client.post(url).json(&prediction_route).send().await {
        Ok(resp) => resp,
        Err(err) => {
            tracing::error!("Error sending prediction request: {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    let status = resp.status();
    if !status.is_success() {
        tracing::error!("Error sending prediction request, status: {}", status);
        return HttpResponse::InternalServerError().finish();
    }

    let resp: Vec<PredictedRouteInfo> = match resp.json().await {
        Ok(resp) => resp,
        Err(err) => {
            tracing::error!("Error sending prediction request {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let mut result: Vec<SegmentWithCongestionLevel> = vec![];
    for segment in resp {
        let idx = match segments
            .iter()
            .position(|ele| ele.properties.segment_id == segment.segment_id)
        {
            Some(idx) => idx,
            None => {
                tracing::error!("Segment id {} have not been found", segment.segment_id);
                return HttpResponse::InternalServerError().finish();
            }
        };
        let temp = &segments[idx];
        let new_segment = SegmentWithCongestionLevel {
            _id: temp._id.clone(),
            _type: temp._type.clone(),
            properties: temp.properties.clone(),
            geometry: temp.geometry.clone(),
            congestion_level: segment.congestion_level,
        };
        result.push(new_segment);
    }

    HttpResponse::Ok().json(result)
}
