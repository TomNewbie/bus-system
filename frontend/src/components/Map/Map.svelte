<script>
	// @ts-nocheck

	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map, Marker, Popup, LngLatBounds } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import { currentIndex, allBusLines, minute } from '../../stores/stores';

	// @ts-ignore
	let map;
	// @ts-ignore
	let mapContainer;
	// @ts-ignore
	let lng, lat, zoom;
	let abortController;

	const congestionColors = {
		0: '#43D224', // Congestion level 1
		1: '#FFE58F', // Congestion level 2
		2: '#FE6240', // Congestion level 3
		3: '#fc7a7a', // Congestion level 4
		4: '#B60606' // Congestion level 5
	};
	let previousIndex;
	$: {
		viewFullMap($allBusLines);
		drawDetailBusline($allBusLines, $currentIndex);
	}
	$: {
		fetchCongestionData($currentIndex, $minute);
	}
	// Load the JSON data
	$: formatedBuslines = $allBusLines;
	var stopsMarker = [];
	const initialState = { zoom: 11 };
	let isFilter = false;

	function getCenterLngLat(formatedBuslines) {
		let lng = 0;
		let lat = 0;
		let length = 0;
		if (formatedBuslines == undefined) return;
		if (initialState.center) return initialState.center;
		formatedBuslines.forEach((formatedBusline) => {
			formatedBusline.forEach((busStop) => {
				busStop.geometry.coordinates.forEach((coordinate) => {
					lng += coordinate[0];
					lat += coordinate[1];
					length++;
				});
			});
		});
		initialState.center = [lng / length, lat / length];
		return initialState.center;
	}

	function updateData() {
		// @ts-ignore
		zoom = map.getZoom();
		// @ts-ignore
		lng = map.getCenter().lng;
		// @ts-ignore
		lat = map.getCenter().lat;
	}

	function removeMarker() {
		stopsMarker.forEach((stopMarker) => stopMarker.remove());
	}

	function setDisableLayer(results, indexToSkip) {
		if (!isFilter) {
			results.forEach((result, routeIndex) => {
				result.forEach((segment, segmentIndex) => {
					const layerId = `route_${routeIndex}`;

					if (indexToSkip !== routeIndex) {
						map.setLayoutProperty(layerId, 'visibility', 'none');
					}
				});
			});
			isFilter = true;
		}
	}

	function viewFullMap(results) {
		if (results == undefined) return;
		deleteCongestionLevel(previousIndex);
		removeMarker();
		if (isFilter) {
			map.flyTo({
				center: getCenterLngLat(results),
				zoom: initialState.zoom
			});
			formatedBuslines.forEach((result, routeIndex) => {
				const layerId = `route_${routeIndex}`;
				map.setLayoutProperty(layerId, 'visibility', 'visible');
			});
		}
		isFilter = false;
	}

	function drawDetailBusline(results, index) {
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
		results[routeNumber].forEach((segment) => {
			let startStopLabel = segment['properties']['start_stop_name'];
			let startStopLngLat = segment['geometry']['coordinates'][0];
			let popup = new Popup({ offset: 25 }).setText(startStopLabel);
			const marker = new Marker().setLngLat(startStopLngLat).setPopup(popup).addTo(map);
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
			.addTo(map);
		bounds.extend(
			result[result.length - 1]['geometry']['coordinates'][
				result[result.length - 1]['geometry']['coordinates'].length - 1
			]
		);
		stopsMarker.push(marker);
		map.fitBounds(bounds, {
			padding: { top: 10, bottom: 25, left: 300, right: 5 }
		});

		setDisableLayer(results, index);
	}

	async function fetchBusLine() {
		let a = [];
		try {
			const response = await fetch('http://localhost:8000/segments');
			if (response.ok) {
				const data = await response.json();
				// Process the data and remove the "_id" attribute
				a = data.map((item) => {
					const { _id, ...itemWithoutId } = item;
					return itemWithoutId;
				});
			} else {
				alert('Request failed with status: ' + response.status);
			}
		} catch (error) {
			alert('Error while fetching data: ' + error);
		}
		const groupedData = {};
		a.forEach((feature) => {
			const shapeId = feature.properties.shape_id;
			if (!groupedData[shapeId]) {
				groupedData[shapeId] = [];
			}
			groupedData[shapeId].push(feature);
		});
		console.log(groupedData);
		allBusLines.set(Object.values(groupedData));
	}

	function deleteCongestionLevel(currentIndex) {
		if (currentIndex == -1 || currentIndex == undefined) return;
		if (abortController) {
			abortController.abort();
		}

		if (!map.getLayer(`segment_0`)) {
			return;
		}

		let currentBusLine = $allBusLines[currentIndex];
		currentBusLine.forEach((segment, segmentIndex) => {
			const layerId = `segment_${segmentIndex}`;
			if (map.getLayer(layerId)) {
				map.removeLayer(layerId);
			}

			if (map.getSource(layerId)) {
				map.removeSource(layerId);
			}
		});
	}

	async function fetchCongestionData(currentIndex, minute) {
		deleteCongestionLevel(previousIndex);
		if (minute == 0) return;
		if (currentIndex == -1 || currentIndex == undefined) return;
		let properties = $allBusLines[currentIndex][0].properties;
		// fetch data
		abortController = new AbortController();

		let a;
		try {
			const response = await fetch(
				`http://localhost:8000/predict?route_id=${properties.route_id}&shape_id=${properties.shape_id}&direction_id=${properties.direction_id}&minute_predict=${minute}`,
				{
					signal: abortController.signal
				}
			);
			if (response.ok) {
				const data = await response.json();
				// Process the data and remove the "_id" attribute
				a = data.map((item) => {
					const { _id, ...itemWithoutId } = item;
					return itemWithoutId;
				});
			} else {
				alert('Request failed with status: ' + response.status);
				return;
			}
		} catch (error) {
			alert('Error while fetching data: ' + error);
			return;
		}
		drawCongestionLevel(a);
	}

	function drawCongestionLevel(currentBusLine) {
		console.log(currentBusLine);
		setDisableLayer($allBusLines, -1);

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
	onMount(async () => {
		await fetchBusLine();

		map = new Map({
			// @ts-ignore
			container: mapContainer,
			accessToken:
				'pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg',
			style: `mapbox://styles/mapbox/streets-v12`,
			// center: initialState.lngLat,
			center: getCenterLngLat($allBusLines),
			zoom: initialState.zoom
		});

		map.on('move', () => {
			updateData();
		});

		map.on('load', () => {
			formatedBuslines.forEach((result, routeIndex) => {
				map.addSource(`route_${routeIndex}`, {
					type: 'geojson',
					data: {
						type: 'FeatureCollection',
						features: result
					}
				});
				map.addLayer({
					id: `route_${routeIndex}`,
					type: 'line',
					source: `route_${routeIndex}`,
					layout: {
						'line-join': 'miter',
						'line-cap': 'round'
					},
					paint: {
						'line-color': '#808080',
						'line-width': 4
					}
				});

				map.on('click', `route_${routeIndex}`, (e) => {
					// Handle click event for this segment
					if (routeIndex === $currentIndex) return;
					currentIndex.set(routeIndex);
				});

				map.on('mouseenter', `route_${routeIndex}`, () => {
					// Change cursor style on hover
					map.getCanvas().style.cursor = 'pointer';
				});

				map.on('mouseleave', `route_${routeIndex}`, () => {
					// Restore cursor style on mouse leave
					map.getCanvas().style.cursor = '';
				});
			});
		});

		map.on('contextmenu', (e) => {
			currentIndex.set(-1);
		});
	});
	onDestroy(() => {
		// @ts-ignore
		if (map) map.remove();
	});
	function doSomething() {
		console.log('asdasd');
	}
</script>

<div>
	<div class="relative min-h-screen min-w-screen">
		<div bind:this={mapContainer} class="map">
			{#if map}
				<div on:custom-event={doSomething} />
				<slot />
			{/if}
		</div>
	</div>
</div>

<style>
	.map {
		position: absolute;
		width: 100%;
		height: 100%;
		bottom: 0;
		top: 0;
		right: 0;
		left: 0;
	}
</style>
