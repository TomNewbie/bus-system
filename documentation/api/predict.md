# Predict API

The Predict endpoint allows users to make predictions using specific models for route information.

#### Endpoint

```
GET /predict/{model}
```

#### Description

This endpoint enables the prediction of route data using the selected model (either LSTM or Random Forest).

#### Parameters

- **`model`** (path parameter)

  - Type: String
  - Description: Specifies the model to be used for prediction. Accepts either `lstm` or `random-forest`.

- **`route_id`** (query parameter)

  - Type: String
  - Description: Identifies the specific route for prediction.

- **`shape_id`** (query parameter)

  - Type: String
  - Description: Represents the shape identifier for the route.

- **`direction_id`** (query parameter)

  - Type: Integer
  - Description: Indicates the direction for the route.

- **`minute_predict`** (query parameter)
  - Type: Integer
  - Description: Specifies the number of minutes into the future for which the prediction is made. For example, minute_predict=10 predicts data for the next 10 minutes

#### Example

```
GET /predict/random-forest?route_id=100007&shape_id=2358&direction_id=1&minute_predict=120
```

This request uses the Random Forest model to predict route data for a specific route ID (100007), shape ID (2358), with direction 1, and predicts data for the next 120 minutes..

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json
- **Details for each returned segment**:

```json
{

  "_id": Object,
  "type": String,
  "properties": {
    "shape_id": String,
    "route_id": String,
    "route_name": String,
    "direction_id": Integer,
    "stop_sequence": Integer,
    "segment_name": String,
    "start_stop_name": String,
    "end_stop_name": String,
    "segment_id": String,
    "start_stop_id": String,
    "end_stop_id": String,
    "distance_m": Float,
  },
  "geometry": {
    "type": String,
    "coordinates": Array,
  },
 "congestion_level": Integer,
}
```

- **Example**: 
```json
[
    {
        "_id": {
            "$oid": "65349d276ddaa83368607e71"
        },
        "type": "Feature",
        "properties": {
            "shape_id": "2358",
            "route_id": "100007",
            "route_name": "7",
            "direction_id": 1,
            "stop_sequence": 1,
            "segment_name": "Köln Zündorf - Köln Rosenhügel",
            "start_stop_name": "Köln Zündorf",
            "end_stop_name": "Köln Rosenhügel",
            "segment_id": "486 - 228",
            "start_stop_id": "486",
            "end_stop_id": "228",
            "distance_m": 1192.040238050357
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [
                    7.049067854428568,
                    50.8660841294039
                ],
                [
                    7.05044,
                    50.86717
                ],
                [
                    7.05885,
                    50.87259
                ],
                [
                    7.05966,
                    50.87347
                ],
                [
                    7.06001,
                    50.87402
                ],
                [
                    7.060046708185053,
                    50.87413746619217
                ]
            ]
        },
        "congestion_level": 0
    },
    {
        "_id": {
            "$oid": "65349d276ddaa83368607e73"
        },
        "type": "Feature",
        "properties": {
            "shape_id": "2358",
            "route_id": "100007",
            "route_name": "7",
            "direction_id": 1,
            "stop_sequence": 2,
            "segment_name": "Köln Rosenhügel - Köln Porz Markt",
            "start_stop_name": "Köln Rosenhügel",
            "end_stop_name": "Köln Porz Markt",
            "segment_id": "228 - 467",
            "start_stop_id": "228",
            "end_stop_id": "467",
            "distance_m": 1280.7577600095783
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [
                    7.060046708185053,
                    50.87413746619217
                ],
                [
                    7.06011,
                    50.87434
                ],
                [
                    7.06019,
                    50.87503
                ],
                [
                    7.06008,
                    50.87566
                ],
                [
                    7.05986,
                    50.87613
                ],
                [
                    7.05935,
                    50.87682
                ],
                [
                    7.05763,
                    50.87872
                ],
                [
                    7.05723,
                    50.87953
                ],
                [
                    7.05723,
                    50.88023
                ],
                [
                    7.05744,
                    50.8808
                ],
                [
                    7.05873,
                    50.8826
                ],
                [
                    7.05924,
                    50.88399
                ],
                [
                    7.059206979981841,
                    50.88499380855203
                ]
            ]
        },
        "congestion_level": 0
    },
    {
        "_id": {
            "$oid": "65349d276ddaa83368607e74"
        },
        "type": "Feature",
        "properties": {
            "shape_id": "2358",
            "route_id": "100007",
            "route_name": "7",
            "direction_id": 1,
            "stop_sequence": 3,
            "segment_name": "Köln Porz Markt - Köln Porz Steinstr.",
            "start_stop_name": "Köln Porz Markt",
            "end_stop_name": "Köln Porz Steinstr.",
            "segment_id": "467 - 466",
            "start_stop_id": "467",
            "end_stop_id": "466",
            "distance_m": 789.4864169071183
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [
                    7.059206979981841,
                    50.88499380855203
                ],
                [
                    7.05919,
                    50.88551
                ],
                [
                    7.05875,
                    50.88636
                ],
                [
                    7.05785,
                    50.88941
                ],
                [
                    7.05751,
                    50.89018
                ],
                [
                    7.0573,
                    50.89057
                ],
                [
                    7.05641,
                    50.89166
                ],
                [
                    7.056244101777437,
                    50.891762015026416
                ]
            ]
        },
        "congestion_level": 0
    },
    ...
]
```

### Errors

- **Status Code**: 500 Internal Server Error
- **Status Code**: 404 Not Found
  - Request: predict/abc?route_id=100007&shape_id=2358&direction_id=1&minute_predict=120
  - Reason: The requested prediction is not supported
  - Resposne: 
    ```json
    {
      "error": "Model abc not supported"
    }
    ```
- **Status Code**: 400 Bad Request
  - Request: predict/random-forest?route_id=adsf&shape_id=2358&direction_id=1&minute_predict=120
  - Reason: String from route_id can not be convert to an integer