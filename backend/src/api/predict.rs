use actix_web::{
    post,
    web::{self, ServiceConfig},
    HttpResponse,
};
use bson::Document;
use serde_json::Value;

pub fn predict_config(cfg: &mut ServiceConfig) {
    cfg.service(web::scope("/predict").service(dummy_predict));
}

// Dummy route to test for connection to tensorflow serving for model deployment
#[post("dummy")]
pub async fn dummy_predict() -> HttpResponse {
    let url = "http://localhost:8501/v1/models/lstm:predict";
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
    let resp: Document = match resp.json().await {
        Ok(resp) => resp,
        Err(err) => {
            tracing::error!("Error sending prediction request {}", err);
            return HttpResponse::InternalServerError().finish();
        }
    };
    HttpResponse::Ok().json(resp)
}
