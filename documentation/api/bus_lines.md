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
    "route_id": 100104,
    "start_stop_name": "Köln Leuchterstr.",
    "end_stop_name": "Köln Am Emberg",
    "agency_name": "KVB Kölner Verkehrs-Betriebe AG"
  },
  {
    "route_id": 100124,
    "start_stop_name": "Köln Breslauer Platz/Hbf",
    "end_stop_name": "Köln Amsterdamer Str./Gürtel",
    "agency_name": "KVB Kölner Verkehrs-Betriebe AG"
  },
  {
    "route_id": 300020,
    "start_stop_name": "Leverkusen Forellental",
    "end_stop_name": "Leverkusen Schöne Aussicht",
    "agency_name": "wupsi wupsi GmbH"
  }
]
```

### Errors

- **Status Code**: 500 Internal Server Error

## Get Bus Line by ID

### Endpoint

- GET /bus-lines/{id}

### Description

Retrieve information about a specific bus line using route ID.

### Parameters

- id (number): ID of the bus line to retrieve.

### Response

- **Status Code**: 200 OK
- **Content Type**: application/json

```json
  {
  "route_id": number,
  "shape_id": "string",
  "start_stop_name": "string",
  "end_stop_name": "string",
  "agency_name": "string",
  "stops": [
            {
                "stop_id": number,
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
    "route_id": 100009,
    "start_stop_name": "Köln Königsforst",
    "end_stop_name": "Köln Röttgensweg",
    "agency_name": "KVB Kölner Verkehrs-Betriebe AG",
    "stops": [
        {
            "stop_id": 533,
            "stop_sequence": 7,
            "stop_name": "Köln Ostheim",
            "stop_lat": 50.929228,
            "stop_lon": 7.041239
        },
        {
            "stop_id": 557,
            "stop_sequence": 1,
            "stop_name": "Köln Königsforst",
            "stop_lat": 50.919729,
            "stop_lon": 7.096903
        },
        {
            "stop_id": 555,
            "stop_sequence": 2,
            "stop_name": "Köln Röttgensweg",
            "stop_lat": 50.920265,
            "stop_lon": 7.090559
        },
        {
            "stop_id": 556,
            "stop_sequence": 3,
            "stop_name": "Köln Rath/Heumar",
            "stop_lat": 50.9203,
            "stop_lon": 7.081941
        },
        {
            "stop_id": 553,
            "stop_sequence": 5,
            "stop_name": "Köln Steinweg",
            "stop_lat": 50.923631,
            "stop_lon": 7.066786
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
