use actix_web::{
    routes, 
    web::{self, Data, ServiceConfig},
    HttpResponse,
};
use bson::{self, doc, Document, Bson};
use futures::TryStreamExt;
use mongodb::{Client, Collection, error::Error};

use crate::models::route_info::RouteInfo;


pub fn segments_config(cfg: &mut ServiceConfig) {
    cfg.service(web::scope("/segments").service(get_segments));
}

async fn fetch_route_infos(db_client: &Data<Client>, nroutes: i64) -> Result<Vec<String>, Error> {
    let col: Collection<RouteInfo> = db_client.database("bus").collection("route_info");
    let limit =  doc!{"$limit": Bson::Int64(nroutes)};
    let pipeline = vec![limit];
    let mut cursor = col.aggregate(pipeline, None).await?;
    let mut result = Vec::new();
    while let Some(doc) = cursor.try_next().await? {
        let route: RouteInfo = bson::from_document(doc)?;
        let id = route.route_id.to_string();
        result.push(id);
    }
    Ok(result)
}

#[routes]
#[get("")]
#[get("/")]
async fn get_segments(db_client: Data<Client>) -> HttpResponse {
    let routes = match fetch_route_infos(&db_client, 1000).await {
        Ok(routes) => routes,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let col: Collection<Document> = db_client.database("bus").collection("segments");
    let cond = doc!{
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
