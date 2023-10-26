<script>
	// @ts-nocheck

	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map, Marker, Popup, NavigationControl, LngLatBounds } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import {
		busLinePopoverVisible,
		currentBusLine,
		currentIndex,
		hehe,
		searchPopoverVisible
	} from '../../stores/stores';
	import { listen } from 'svelte/internal';

	// @ts-ignore
	let map;
	// @ts-ignore
	let mapContainer;
	// @ts-ignore
	let lng, lat, zoom;

	let data = [];
	$: {
		viewFullMap(formatedBuslines);
		drawDetailBusline(formatedBuslines, $currentIndex);
	}

	// Load the JSON data
	$: formatedBuslines = $hehe;
	let isFilter = false;
	var stopsMarker = [];
	const initialState = { zoom: 11 };

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

	function getRainbowColor(index) {
		const lgbtColorsHex = ['#FF0018', '#FFA52D', '#FFFF41', '#008018', '#0000F9', '#86007D'];
		return lgbtColorsHex[index % lgbtColorsHex.length];
	}

	function removeMarker() {
		stopsMarker.forEach((stopMarker) => stopMarker.remove());
	}

	function setDisableLayer(results, indexToSkip) {
		if (!isFilter)
			results.forEach((result, index) => {
				console.log(result);
				if (index !== indexToSkip) {
					map.setLayoutProperty(`route ${index}`, 'visibility', 'none');
				}
			});
		isFilter = true;
	}

	function viewFullMap(results) {
		if (results == undefined) return;
		removeMarker();
		if (isFilter) {
			map.flyTo({
				center: getCenterLngLat(results),
				zoom: initialState.zoom
			});
			results.forEach((result, index) =>
				map.setLayoutProperty(`route ${index}`, 'visibility', 'visible')
			);
			searchPopoverVisible.set(true);
			busLinePopoverVisible.set(false);
		}
		isFilter = false;
	}

	function drawDetailBusline(results, index) {
		if (results == undefined) return;
		if (index == -1 || index == undefined) return;
		searchPopoverVisible.set(false);
		busLinePopoverVisible.set(true);
		currentBusLine.set(results[index]);
		const routeNumber = index;
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

		const fullData = Object.values(groupedData);
		hehe.set(fullData.slice(0, 70));
	}

	onMount(async () => {
		// const unsubscribe = listen(window, 'custom-event', handleDraw);
		await fetchBusLine();

		map = new Map({
			// @ts-ignore
			container: mapContainer,
			accessToken:
				'pk.eyJ1IjoidGhhbmgzMDAxIiwiYSI6ImNsbjMwMzlsczBlMTQycm5rY3p2cTltdXIifQ.n7uqai-eq-VyjI9-BtJxYg',
			style: `mapbox://styles/mapbox/streets-v12`,
			// center: initialState.lngLat,
			center: getCenterLngLat($hehe),
			zoom: initialState.zoom
		});

		map.on('move', () => {
			updateData();
		});
		// map.addControl(new NavigationControl());

		map.on('load', () => {
			formatedBuslines.forEach((result, index) => {
				map.addSource(`route ${index}`, {
					type: 'geojson',
					data: {
						type: 'FeatureCollection',
						features: result
					}
				});

				let color = getRainbowColor(index);

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
						'line-width': 4
					}
				});
				map.on('click', `route ${index}`, (e) => {
					if (index == $currentIndex) return;
					currentIndex.set(index);
				});
				map.on('mouseenter', `route ${index}`, () => {
					map.getCanvas().style.cursor = 'pointer';
				});
				map.on('mouseleave', `route ${index}`, () => {
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
