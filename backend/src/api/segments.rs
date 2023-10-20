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
    let limit_pipeline = doc! {"$limit": 200};
    let group_pipeline = doc! {"$group": {
        "_id": {
            "route_id": "$properties.route_id"
        },
        "documents": {"$push": "$$ROOT"},
    }};
    let unwind_pipeline = doc! {"$unwind":  "$documents"};
    let shape_group_pipeline = doc! {
        "$group": {
            "_id": "$_id",
            "shape_id": { "$first": "$documents.properties.shape_id" },
            "documents": { "$push": "$documents" }
        }
    };
    let project_pipeline = doc! {
        "$project": {
            "_id": 0,
            "documents": 1,
        }
    };
    let replace_root_pipeline = doc! {
        "$replaceRoot": {
            "newRoot": "$documents",
        }
    };
    let pipeline = vec![
        limit_pipeline,
        group_pipeline,
        unwind_pipeline.clone(),
        shape_group_pipeline,
        project_pipeline,
        unwind_pipeline,
        replace_root_pipeline,
    ];
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
