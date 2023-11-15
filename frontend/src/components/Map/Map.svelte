<script lang="ts">
	// @ts-nocheack
	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import { currentIndex, busNetwork, minute } from '../../stores/stores';
	import { getCenterLngLat } from '../../utils/map';
	import { fetchBusLine } from '../../services/map';
	import { drawDetailBusline, viewFullMap } from '../../controller/visualization';
	import { fetchCongestionData } from '../../controller/congestion';

	let map: Map;
	let mapContainer: Map;
	let lng, lat, zoom;
	const mapConfig: MapState = { zoom: 11 };

	$: {
		viewFullMap($busNetwork, map, mapConfig);
		drawDetailBusline($busNetwork, $currentIndex, map);
	}
	$: {
		fetchCongestionData($busNetwork, $currentIndex, $minute, map);
	}
	// Load the JSON data
	$: formatedBuslines = $busNetwork;

	function updateData() {
		zoom = map.getZoom();
		lng = map.getCenter().lng;
		lat = map.getCenter().lat;
	}

	onMount(async () => {
		busNetwork.set(await fetchBusLine());

		map = new Map({
			container: mapContainer,
			accessToken:
				'pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg',
			style: `mapbox://styles/mapbox/streets-v12`,
			center: getCenterLngLat(mapConfig, $busNetwork),
			zoom: mapConfig.zoom
		});

		map.on('move', () => {
			updateData();
		});

		map.on('load', () => {
			formatedBuslines.forEach((busLine, routeIndex) => {
				map.addSource(`route_${routeIndex}`, {
					type: 'geojson',
					data: {
						type: 'FeatureCollection',
						features: busLine
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

				map.on('click', `route_${routeIndex}`, () => {
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

		map.on('contextmenu', (e: any) => {
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
