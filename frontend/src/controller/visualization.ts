import pkg from 'mapbox-gl';
import type { Map } from 'mapbox-gl';
const { LngLatBounds, Popup, Marker } = pkg;
import { getCenterLngLat } from '../utils/mapUtils';
import { deleteCongestionLevel } from './congestion';
import { countReroute, canReroute, reroutingMode } from '../stores/stores';
import { deleteRerouteLayer } from './rerouting';

var stopsMarker: any[] = [];

export function drawDetailBusline(busNetwork: BusNetwork, index: number, map: Map) {
	if (busNetwork == undefined) return;
	if (index == -1 || index == undefined) return;
	const routeNumber = index;

	const bounds = new LngLatBounds(
		busNetwork[routeNumber][0].geometry.coordinates[0],
		busNetwork[routeNumber][busNetwork[routeNumber].length - 1].geometry.coordinates[
			busNetwork[routeNumber][busNetwork[routeNumber].length - 1].geometry.coordinates.length - 1
		]
	);
	let busLine = busNetwork[routeNumber];
	busLine.sort((busStopA, busStopB) => busStopA.properties.stop_sequence - busStopB.properties.stop_sequence)

	// Create marker and add Bound to fit line
	busLine.forEach((segment) => {
		
		let startStopLabel = segment['properties']['start_stop_name'];
		let startStopLngLat = segment['geometry']['coordinates'][0];
		let popup = new Popup({ offset: 25 }).setText(startStopLabel);
		const marker = new Marker().setLngLat(startStopLngLat).setPopup(popup).addTo(map);
		stopsMarker.push(marker);
		bounds.extend(startStopLngLat);
	});

	let endStopLabel = busLine[busLine.length - 1]['properties']['end_stop_name'];
	let endStopLngLat = busLine[busLine.length - 1]['geometry']['coordinates'][
		busLine[busLine.length - 1]['geometry']['coordinates'].length - 1
	]
	let popup = new Popup({ offset: 25 }).setText(endStopLabel);
	const marker1 = new Marker().setLngLat(endStopLngLat).setPopup(popup).addTo(map);
	stopsMarker.push(marker1);
	bounds.extend(endStopLngLat);

	map.fitBounds(bounds, {
		padding: { top: 100, bottom: 25, left: 300, right: 5 }
	});

	setDisableLayer(busNetwork, index, map);
}

export function setDisableLayer(busNetwork: BusNetwork, indexToSkip: number, map: Map) {
	busNetwork.forEach((result, routeIndex) => {
		result.forEach((segment, segmentIndex) => {
			const layerId = `route_${routeIndex}`;

			if (indexToSkip !== routeIndex) {
				// @ts-ignore
				map.setLayoutProperty(layerId, 'visibility', 'none');
			}
		});
	});
}

export function viewFullMap(busNetwork: BusNetwork, map: Map, mapConfig: MapState) {
	if (busNetwork == undefined) return;
	if (map == undefined) return;
	if (!map.getLayer(`route_0`)) return;

	deleteCongestionLevel(busNetwork, map);
	deleteRerouteLayer(map)
	countReroute.set(0);
	canReroute.set(false);
	reroutingMode.set(false);

	removeMarker();

	map.flyTo({
		center: getCenterLngLat(mapConfig, busNetwork),
		zoom: 11
	});

	busNetwork.forEach((_, routeIndex) => {
		const layerId = `route_${routeIndex}`;

		map.setLayoutProperty(layerId, 'visibility', 'visible');
	});
}

function removeMarker() {
	stopsMarker.forEach((stopMarker) => stopMarker.remove());
}


