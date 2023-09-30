# Bus Lines API

The Bus Lines API provides endpoints to retrieve information about bus lines.

## Get All Bus Lines

### Endpoint

- GET /bus-lines

### Description

Retrieve a list of all bus lines.

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json

```json
[
  {
    "route_id": number,
    "trip_id": "string",
    "shape_id": "string",
    "start_stop_name": "string",
    "end_stop_name": "string",
    "agency_name": "string"
  }
]
```

- Example
```json
[
    {
        "route_id": 2400703,
        "trip_id": "10-703-024-7544.2.22:092800-9-1_1C283E93-0335-4F49-9EAB-AF41012CC60B",
        "start_stop_name": "Brühl Engeldorfer Str.",
        "end_stop_name": "Brühl Telekom",
        "agency_name": "StWB Stadtwerke Brühl"
    },
    {
        "route_id": 2400703,
        "trip_id": "1-703-024-735.2.22:064900-10-1_475D6B65-EEB6-461C-8EF9-AF41012CC737",
        "start_stop_name": "Brühl Mitte",
        "end_stop_name": "Brühl Nord",
        "agency_name": "StWB Stadtwerke Brühl"
    },
    {
        "route_id": 2400703,
        "trip_id": "1002-703-024-7539.2.22:150000-8-1_25518188-F495-4CCB-8E92-AF41012CC737",
        "start_stop_name": "Brühl Telekom",
        "end_stop_name": "Brühl Wesselinger Str.",
        "agency_name": "StWB Stadtwerke Brühl"
    },
]
```
### Errors
- **Status Code**: 500 Internal Server Error


## Get Bus Line by ID

### Endpoint

- GET /bus-lines/{id}

### Description

Retrieve information about a specific bus line using its ID.

### Parameters

- id (path): ID of the bus line to retrieve.

### Response

- **Status Code**: 200 OK
- **Content Type**: application/json

```json
  {
  "route_id": number,
  "trip_id": "string",
  "shape_id": "string",
  "start_stop_name": "string",
  "end_stop_name": "string",
  "agency_name": "string",
  "stops": [
            {
                "stop_id": number,
                "arrival_time": "string",
                "departure_time": "string",
                "stop_sequence": number,
                "stop_name": "string",
                "stop_lat": double,
                "stop_lon": double,
            },
        ]
  }
```
- Example:
```json
{
    "route_id": 2400703,
    "trip_id": "10-703-024-7544.2.22:092800-9-1_1C283E93-0335-4F49-9EAB-AF41012CC60B",
    "start_stop_name": "Brühl Engeldorfer Str.",
    "end_stop_name": "Brühl Telekom",
    "agency_name": "StWB Stadtwerke Brühl",
    "stops": [
        {
            "stop_id": 735,
            "arrival_time": "09:42:00",
            "departure_time": "09:42:00",
            "stop_sequence": 9,
            "stop_name": "Brühl Mitte",
            "stop_lat": 50.828921,
            "stop_lon": 6.899026
        },
        {
            "stop_id": 734,
            "arrival_time": "09:40:00",
            "departure_time": "09:40:00",
            "stop_sequence": 8,
            "stop_name": "Brühl Nord",
            "stop_lat": 50.834277,
            "stop_lon": 6.901641
        },
        {
            "stop_id": 5353,
            "arrival_time": "09:37:00",
            "departure_time": "09:37:00",
            "stop_sequence": 7,
            "stop_name": "Brühl Kölnstr./Comesstr.",
            "stop_lat": 50.831617,
            "stop_lon": 6.906175
        },
        ...
    ]
}
```

### Errors
- **Status Code**: 400 Bad Request
  - **Response**: invalid ID.
- **Status Code**: 404 Not Found
  - **Response**: ID not found.
- **Status Code**: 500 Internal Server Error
