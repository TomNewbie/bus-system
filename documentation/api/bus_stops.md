# Bus Stops API

The Bus Stops API provides endpoints to retrieve information about bus stops.

## Get All Bus stops

### Endpoint

- GET /bus-stops

### Description

Retrieve a list of all bus stops.

### Response

- **Status Code:** 200 OK
- **Content Type:** application/json

```json
[
  {
    "stop_id": number,
    "stop_name": "string",
    "stop_lat": double,
    "stop_lon": double,
  }
]
```

- Example

```json
[
  {
    "stop_id": 43,
    "stop_name": "Bonn Propsthof Nord",
    "stop_lat": 50.739096,
    "stop_lon": 7.073507
  },
  {
    "stop_id": 735,
    "stop_name": "Brühl Mitte",
    "stop_lat": 50.828921,
    "stop_lon": 6.899026
  },
  {
    "stop_id": 1110,
    "stop_name": "Bonn Wilhelmsplatz",
    "stop_lat": 50.740145,
    "stop_lon": 7.098919
  }
]
```

### Errors

- **Status Code**: 500 Internal Server Error

## Get Bus Stop by ID

### Endpoint

- GET /bus-stops/{id}

### Description

Retrieve information about a specific bus stop using its ID.

### Parameters

- id (number): ID of the bus stop to retrieve.

### Response

- **Status Code**: 200 OK
- **Content Type**: application/json

```json
  {
    "stop_id": number,
    "stop_name": "string",
    "stop_lat": double,
    "stop_lon": double,
    "routes": [
            {
                "route_id": number,
                "shape_id": "string",
                "start_stop_name": "string",
                "end_stop_name": "string",
                "agency_name": "string"
            },
        ]
  }
```

- Example:

```json
{
  "stop_id": 43,
  "stop_name": "Bonn Propsthof Nord",
  "stop_lat": 50.739096,
  "stop_lon": 7.073507,
  "routes": [
    {
      "route_id": 600633,
      "shape_id": 3124,
      "start_stop_name": "Bonn Gerhart-Hauptmann-Str.",
      "end_stop_name": "Bonn Endenich Nord Bf",
      "agency_name": "SWB Stadtwerke Bonn Verkehrs GmbH"
    }
  ]
}
```

### Errors

- **Status Code**: 400 Bad Request
  - **Response**: invalid ID.
- **Status Code**: 404 Not Found
  - **Response**: ID not found.
- **Status Code**: 500 Internal Server Error
