interface GeoJson {
	type: 'Feature';
	properties: Properties;
	geometry: Geometry;
}

interface GeoJsonWithCongestionLevel extends GeoJson {
	congestion_level: number;
}

interface GeoJsonWithId extends GeoJson {
	_id: {
		$oid: string;
	};
}

interface GeoJsonGroupByShapeId {
	[key: number]: GeoJson[];
}
interface Properties {
	shape_id: string;
	route_id: string;
	route_name: string;
	direction_id: number;
	stop_sequence: number;
	segment_name: string;
	start_stop_name: string;
	end_stop_name: string;
	segment_id: string;
	start_stop_id: string;
	end_stop_id: string;
	distance_m: number;
}

interface Geometry {
	type: string;
	coordinates: Coordinate[];
}

type Coordinate = [number, number];

interface MapState {
	zoom: number;
	center?: Coordinate;
}

type Segment = GeoJson;
type BusLine = GeoJson[];
type BusNetwork = BusLine[];
type BusLineWithCongestionLevel = GeoJsonWithCongestionLevel[];
