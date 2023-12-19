use actix_web::{
    routes,
    web::{self, Data, ServiceConfig},
    HttpRequest, HttpResponse,
};
use bson::{self, doc, Bson, Document};
use futures::TryStreamExt;
use mongodb::{error::Error, Client, Collection, Database};

use crate::{models::route_info::RouteInfo, utils::country_to_db_name};

pub fn segments_config(cfg: &mut ServiceConfig) {
    cfg.service(web::scope("/segments").service(get_segments));
}

async fn fetch_route_infos(db: &Database, nroutes: i64) -> Result<Vec<String>, Error> {
    let col: Collection<RouteInfo> = db.collection("route_info");
    let limit = doc! {"$limit": Bson::Int64(nroutes)};
    let pipeline = vec![limit];
    let mut cursor = col.aggregate(pipeline, None).await?;
    let mut result = Vec::new();
    while let Some(doc) = cursor.try_next().await? {
        let route: RouteInfo = bson::from_document(doc)?;
        let id = route.route_id;
        result.push(id);
    }
    Ok(result)
}

#[routes]
#[get("")]
#[get("/")]
async fn get_segments(req: HttpRequest, db_client: Data<Client>) -> HttpResponse {
    let country = req.match_info().get("country").unwrap();
    let db_name = match country_to_db_name(&country) {
        Some(name) => name,
        None => {
            return HttpResponse::NotFound().finish();
        }
    };
    let db = db_client.database(&db_name);
    let routes = match fetch_route_infos(&db, 1000).await {
        Ok(routes) => routes,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let col: Collection<Document> = db.collection("segments");
    let cond = doc! {
        "properties.route_id": {
            "$in": routes,
        }
    };
    let cursor = match col.find(cond, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::NotFound().finish();
        }
    };
    let segments: Vec<Document> = match cursor.try_collect().await {
        Ok(segments) => segments,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(segments)
}
