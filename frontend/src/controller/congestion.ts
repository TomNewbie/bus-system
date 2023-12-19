import type { Map } from 'mapbox-gl';
import { setDisableLayer } from './visualization';
import { fetchCongestionDataByBusline } from '../services/mapServices';
import { canReroute, isToastShowed, reroutingMode } from '../stores/stores';

let abortController: AbortController;
let previousIndex = -1;
const congestionColors: {
	[key: number]: string;
} = {
	0: '#43D224', // Congestion level 1
	1: '#FFE58F', // Congestion level 2
	2: '#FFA500', // Congestion level 3
	3: '#FC7A7A', // Congestion level 4
	4: '#B60606' // Congestion level 5
};

function drawCongestionLevel(
	busNetwork: BusNetwork,
	currentBusLine: BusLineWithCongestionLevel,
	map: Map
) {
	if (currentBusLine == undefined) return;
	setDisableLayer(busNetwork, -1, map);

	currentBusLine.forEach((segment, segmentIndex) => {
		// Access the congestion level of the segment
		const congestionLevel = segment.congestion_level;

		// Determine the color based on congestion level
		const color = congestionColors[congestionLevel];

		// Create a source and layer for each segment
		map.addSource(`segment_${segmentIndex}`, {
			type: 'geojson',
			data: {
				type: 'FeatureCollection',
				//@ts-ignore
				features: [segment]
			}
		});

		map.addLayer({
			id: `segment_${segmentIndex}`,
			type: 'line',
			source: `segment_${segmentIndex}`,
			layout: {
				'line-join': 'miter',
				'line-cap': 'round'
			},
			paint: {
				'line-color': color,
				'line-width': 4
			}
		});
	});
}

export async function fetchCongestionData(
	busNetwork: BusNetwork,
	currentIndex: number,
	minute: number,
	map: Map,
	model: string
) {
	if (busNetwork == undefined) return;
	if (currentIndex == -1 || currentIndex == undefined) return;
	deleteCongestionLevel(busNetwork, map);
	setDisableLayer(busNetwork, currentIndex, map);
	if (minute == 0) return;
	if (currentIndex == -1 || currentIndex == undefined) return;
	previousIndex = currentIndex;
	let properties = busNetwork[currentIndex][0].properties;
	// fetch data
	abortController = new AbortController();

	let result = await fetchCongestionDataByBusline(
		model,
		properties.route_id,
		properties.shape_id,
		properties.direction_id,
		minute,
		abortController
	);
	//toast
	if (result != null) {
		isToastShowed.set(true);
		canReroute.set(true);
		drawCongestionLevel(busNetwork, result, map);
	}
}

export function deleteCongestionLevel(busNetwork: BusNetwork, map: Map) {
	if (previousIndex == -1 || previousIndex == undefined) return;
	if (abortController) {
		abortController.abort();
	}

	if (!map.getLayer(`segment_0`)) {
		return;
	}

	let currentBusLine = busNetwork[previousIndex];
	currentBusLine.forEach((_, segmentIndex) => {
		const layerId = `segment_${segmentIndex}`;
		if (map.getLayer(layerId)) {
			map.removeLayer(layerId);
		}

		if (map.getSource(layerId)) {
			map.removeSource(layerId);
		}
	});
}
