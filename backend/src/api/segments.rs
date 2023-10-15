use actix_web::{
    routes,
    web::{self, Data, ServiceConfig},
    HttpResponse,
};
use bson::{doc, Document};
use futures::TryStreamExt;
use mongodb::{Client, Collection};

pub fn segments_config(cfg: &mut ServiceConfig) {
    cfg.service(web::scope("/segments").service(get_200_segments));
}

#[routes]
#[get("")]
#[get("/")]
async fn get_200_segments(db_client: Data<Client>) -> HttpResponse {
    let col: Collection<Document> = db_client.database("bus").collection("segments");
    let pipeline = vec![doc! {"$limit": 200}];
    let cursor = match col.aggregate(pipeline, None).await {
        Ok(cursor) => cursor,
        Err(err) => {
            tracing::error!("Failed to execute the query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    let bus_lines: Vec<Document> = match cursor.try_collect().await {
        Ok(lines) => lines,
        Err(err) => {
            tracing::error!("Failed to execute query: {:?}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };

    HttpResponse::Ok().json(bus_lines)
}
