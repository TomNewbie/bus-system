<script lang="ts">
	// @ts-nocheack
	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import {
		currentIndex,
		busNetwork,
		minute,
		model,
		start_stop_lon_lat,
		end_stop_lon_lat
	} from '../../stores/stores';
	import { getCenterLngLat } from '../../utils/mapUtils';
	import { fetchBusLine } from '../../services/mapServices';
	import { drawDetailBusline, viewFullMap } from '../../controller/visualization';
	import { fetchCongestionData } from '../../controller/congestion';
	import { fetchReroute } from '../../controller/rerouting';

	import LoadingScreen from '../UI/LoadingScreen.svelte';

	let map: Map;
	let mapContainer: Map;
	let lng, lat, zoom;
	const mapConfig: MapState = { zoom: 9 };
	export let api = '';

	$: {
		viewFullMap($busNetwork, map, mapConfig);
		drawDetailBusline($busNetwork, $currentIndex, map);
	}
	$: fetchCongestionData(api, $busNetwork, $currentIndex, $minute, map, $model);
	$: fetchReroute($start_stop_lon_lat, $end_stop_lon_lat, map);
	// Load the JSON data
	$: formatedBuslines = $busNetwork;

	function updateData() {
		zoom = map.getZoom();
		lng = map.getCenter().lng;
		lat = map.getCenter().lat;
	}

	let isMapLoading = true;
	onMount(async () => {
		busNetwork.set(await fetchBusLine(api));

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

		isMapLoading = false;
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
		if (map) map.remove();
	});
</script>

<div>
	<div class="relative min-h-screen min-w-screen">
		{#if isMapLoading}
			<!-- Show loading UI while the map is loading -->
			<LoadingScreen />
		{/if}
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
