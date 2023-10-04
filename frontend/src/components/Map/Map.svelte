<script>
	// @ts-nocheck

	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map, Marker } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';

	// @ts-ignore
	let map;
	// @ts-ignore
	let mapContainer;
	// @ts-ignore
	let lng, lat, zoom;

	lng = 7;
	lat = 50.7;
	zoom = 9;

	function updateData() {
		// @ts-ignore
		zoom = map.getZoom();
		// @ts-ignore
		lng = map.getCenter().lng;
		// @ts-ignore
		lat = map.getCenter().lat;
	}

	onMount(() => {
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

		map.on('move', () => {
			updateData();
		});
		var routeCoordinates = [
			[7.062208, 50.735586],
			[7.06063, 50.735969],
			[7.06481, 50.73665],
			[7.069601, 50.737406],
			[7.073507, 50.739096],
			[7.075749, 50.740487],
			[7.074327, 50.74272],
			[7.080835, 50.744161],
			[7.085753, 50.745455],
			[7.091044, 50.743293],
			[7.096098, 50.741879],
			[7.098919, 50.740145],
			[7.102483, 50.737468],
			[7.116546, 50.737927],
			[7.117181, 50.736636],
			[7.12065, 50.737124],
			[7.123593, 50.737572],
			[7.127652, 50.738477],
			[7.13033, 50.736761],
			[7.139913, 50.737018],
			[7.142498, 50.73497],
			[7.14563, 50.733303],
			[7.148731, 50.730342],
			[7.15079, 50.725953],
			[7.153079, 50.72397],
			[7.155135, 50.722377]
		]

		map.on('load', () => {
			map.addSource('route', {
				'type': 'geojson',
				'data': {
					'type': 'Feature',
					'properties': {},
					'geometry': {
						'type': 'LineString',
						'coordinates': routeCoordinates
					}
				}
			});
			map.addLayer({
				'id': 'route',
				'type': 'line',
				'source': 'route',
				'layout': {
					'line-join': 'round',
					'line-cap': 'round'
				},
				'paint': {
					'line-color': '#888',
					'line-width': 8
				}
			});
		});
		routeCoordinates.forEach(routeCoordinate => new Marker()
				.setLngLat(routeCoordinate)
				.addTo(map))
		// map.addLayer({
		// 	id: 'bus-route',
		// 	type: 'line',
		// 	source: {
		// 		type: 'geojson',
		// 		data: {
		// 			type: 'Feature',
		// 			properties: {},
		// 			geometry: {
		// 				type: 'LineString',
		// 				coordinates: routeCoordinates
		// 			}
		// 		}
		// 	},
		// 	paint: {
		// 		'line-color': 'blue',
		// 		'line-width': 2
		// 	}
		// });
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
