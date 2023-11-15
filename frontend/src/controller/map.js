// @ts-ignore
// @ts-ignore
import { Map, Marker, Popup, LngLatBounds } from 'mapbox-gl';
import { getCenterLngLat } from '../utils/map';

let isFilter = false;
/**
 * @type {Marker[]}
 */
var stopsMarker = [];
// @ts-ignore
let previousIndex;
// @ts-ignore
export function drawDetailBusline(results, index, map) {
	// @ts-ignore
	if (results == undefined) return;
	if (index == -1 || index == undefined) return;
	const routeNumber = index;
	previousIndex = index;
	const bounds = new LngLatBounds(
		results[routeNumber][0].geometry.coordinates[0],
		results[routeNumber][results[routeNumber].length - 1].geometry.coordinates[
			results[routeNumber][results[routeNumber].length - 1].geometry.coordinates.length - 1
		]
	);

	// Create marker and add Bound to fit line
	// @ts-ignore
	results[routeNumber].forEach((segment) => {
		let startStopLabel = segment['properties']['start_stop_name'];
		let startStopLngLat = segment['geometry']['coordinates'][0];
		let popup = new Popup({ offset: 25 }).setText(startStopLabel);
		// @ts-ignore
		const marker = new Marker().setLngLat(startStopLngLat).setPopup(popup).addTo(map);
		// @ts-ignore
		stopsMarker.push(marker);
		bounds.extend(segment['geometry']['coordinates'][0]);
	});

	let result = results[routeNumber];
	let endStopLabel = result[result.length - 1]['properties']['end_stop_name'];

	let popup = new Popup({ offset: 25 }).setText(endStopLabel);
	const marker = new Marker()
		.setPopup(popup)
		.setLngLat(
			result[result.length - 1]['geometry']['coordinates'][
				result[result.length - 1]['geometry']['coordinates'].length - 1
			]
		)
		// @ts-ignore
		.addTo(map);
	bounds.extend(
		result[result.length - 1]['geometry']['coordinates'][
			result[result.length - 1]['geometry']['coordinates'].length - 1
		]
	);
	// @ts-ignore
	stopsMarker.push(marker);
	// @ts-ignore
	map.fitBounds(bounds, {
		padding: { top: 10, bottom: 25, left: 300, right: 5 }
	});

	// @ts-ignore
	setDisableLayer(results, index, map);
}

// @ts-ignore
export function setDisableLayer(results, indexToSkip, map) {
	if (!isFilter) {
		// @ts-ignore
		results.forEach((result, routeIndex) => {
			// @ts-ignore
			// @ts-ignore
			// @ts-ignore
			result.forEach((segment, segmentIndex) => {
				const layerId = `route_${routeIndex}`;

				if (indexToSkip !== routeIndex) {
					// @ts-ignore
					map.setLayoutProperty(layerId, 'visibility', 'none');
				}
			});
		});
		isFilter = true;
	}
}

// @ts-ignore
export function viewFullMap(results, map) {
	if (results == undefined) return;
	// @ts-ignore
	deleteCongestionLevel(previousIndex, map);
	// @ts-ignore
	removeMarker();
	if (isFilter) {
		// @ts-ignore
		map.flyTo({
			// @ts-ignore
			center: getCenterLngLat(results),
			// @ts-ignore
			zoom: 11
		});
		// @ts-ignore
		// @ts-ignore
		results.forEach((result, routeIndex) => {
			const layerId = `route_${routeIndex}`;
			// @ts-ignore
			map.setLayoutProperty(layerId, 'visibility', 'visible');
		});
	}
	isFilter = false;
}

// @ts-ignore
export function deleteCongestionLevel(currentIndex, map) {
	if (currentIndex == -1 || currentIndex == undefined) return;
	// @ts-ignore
	// if (abortController) {
	// 	// @ts-ignore
	// 	abortController.abort();
	// }

	// @ts-ignore
	if (!map.getLayer(`segment_0`)) {
		return;
	}

	// @ts-ignore
	let currentBusLine = $allBusLines[currentIndex];
	// @ts-ignore
	currentBusLine.forEach((segment, segmentIndex) => {
		const layerId = `segment_${segmentIndex}`;
		// @ts-ignore
		if (map.getLayer(layerId)) {
			// @ts-ignore
			map.removeLayer(layerId);
		}

		// @ts-ignore
		if (map.getSource(layerId)) {
			// @ts-ignore
			map.removeSource(layerId);
		}
	});
}

function removeMarker() {
	stopsMarker.forEach((stopMarker) => stopMarker.remove());
}
