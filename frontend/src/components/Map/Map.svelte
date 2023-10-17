<script>
	// @ts-nocheck

	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map, Marker, Popup, NavigationControl, LngLatBounds } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import createCustomMarkerForSegment from './MapMarker.svelte';
	import Button from '../Button.svelte';

	// @ts-ignore
	let map;
	// @ts-ignore
	let mapContainer;
	// @ts-ignore
	let lng, lat, zoom;

	lng = 7;
	lat = 50.7;
	zoom = 9;
	let data = [];

	// Load the JSON data
	$: busline = [];
	var stopsMarker = [];
	let lineConnect;
	let lineConnect2 = [
		[7.056734830056906, 51.072861874030004],
		[7.05701, 51.07234],
		[7.05708, 51.07176],
		[7.05645, 51.071],
		[7.05628, 51.07055],
		[7.0565, 51.07027],
		[7.05732, 51.06969],
		[7.057873856041132, 51.068748444730076]
	];
	function convertToCoordinate() {
		// const stop_coor = jsonData.stops.map(stop => [stop.stop_lon, stop.stop_lat]);
		// const shape_coor = jsonData.shapes.map(shape => [shape.shape_pt_lon, shape.shape_pt_lat]);
		// stopsMarker = stop_coor;
		// console.log(shape_coor);
		// // lineConnect = stopsMarker.concat(shape_coor);
		// lineConnect = shape_coor;
		// console.log(stopsMarker);
		lineConnect = [
			[7.062356765039729, 51.073037929625428],
			[7.06211, 51.07288],
			[7.06098, 51.07365],
			[7.0604, 51.07388],
			[7.05957, 51.07403],
			[7.05877, 51.07393],
			[7.05793, 51.07353],
			[7.05719, 51.07347],
			[7.05673, 51.07329],
			[7.05672, 51.07289],
			[7.056734830056906, 51.072861874030004]
		];
		stopsMarker = lineConnect;
	}
	// Call the function to load the data
	convertToCoordinate();
	function updateData() {
		// @ts-ignore
		zoom = map.getZoom();
		// @ts-ignore
		lng = map.getCenter().lng;
		// @ts-ignore
		lat = map.getCenter().lat;
	}
	function getRainbowColor(index) {
		const lgbtColorsHex = ['#FF0018', '#FFA52D', '#FFFF41', '#008018', '#0000F9', '#86007D'];
		return lgbtColorsHex[index % lgbtColorsHex.length];
	}
	function drawInteractiveBusline(results, customColor) {
		map.on('load', () => {
			results.forEach((result, index) => {
				map.addSource(`route ${index}`, {
					type: 'geojson',
					data: {
						type: 'FeatureCollection',
						features: result
					}
				});
				const color = customColor ?? getRainbowColor(index);
				map.addLayer({
					id: `route ${index}`,
					type: 'line',
					source: `route ${index}`,
					layout: {
						'line-join': 'miter',
						'line-cap': 'round'
					},
					paint: {
						'line-color': color,
						'line-width': 8
					}
				});
				map.on('click', `route ${index}`, (e) => {
					const routeNumber = index;
					const bounds = new LngLatBounds(
						results[routeNumber][0].geometry.coordinates[0],
						results[routeNumber][results[routeNumber].length - 1].geometry.coordinates[
							results[routeNumber][results[routeNumber].length - 1].geometry.coordinates.length - 1
						]
					);
					map.fitBounds(bounds, {
						padding: 30
					});
					results[routeNumber].forEach((segment) => {
						let startStopLabel = segment['properties']['start_stop_name'];
						let startStopLngLat = segment['geometry']['coordinates'][0];
						let popup = new Popup({ offset: 25 }).setText(startStopLabel);
						new Marker().setLngLat(startStopLngLat).setPopup(popup).addTo(map);
					});
					let result = results[routeNumber];
					let endStopLabel = result[result.length - 1]['properties']['end_stop_name'];

					let popup = new Popup({ offset: 25 }).setText(endStopLabel);
					new Marker()
						.setPopup(popup)
						.setLngLat(
							result[result.length - 1]['geometry']['coordinates'][
								result[result.length - 1]['geometry']['coordinates'].length - 1
							]
						)
						.addTo(map);

					drawInteractiveBusline(result[routeNumber]);
				});
				map.on('mouseenter', `route ${index}`, () => {
					map.getCanvas().style.cursor = 'pointer';
				});
				map.on('mouseleave', `route ${index}`, () => {
					map.getCanvas().style.cursor = '';
				});
			});
		});
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

		return Object.values(groupedData);
	}
	onMount(async () => {
		// @ts-ignore
		const initialState = { lng: lng, lat: lat, zoom: zoom };

		map = new Map({
			// @ts-ignore
			container: mapContainer,
			accessToken:
				'pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg',
			style: `mapbox://styles/mapbox/outdoors-v11`,
			center: [initialState.lng, initialState.lat],
			zoom: initialState.zoom
		});
		map.on('dblclick', (e) => {
			console.log(`A dblclick event has occurred at ${e.lngLat}`);
		});
		map.on('move', () => {
			updateData();
		});
		map.addControl(new NavigationControl());

		busline = await fetchBusLine();
		drawInteractiveBusline(busline);
	});
	onDestroy(() => {
		// @ts-ignore
		if (map) map.remove();
	});
</script>

<div>
	<div class="relative min-h-screen min-w-screen">
		<div bind:this={mapContainer} class="map">
			{#if map}
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
