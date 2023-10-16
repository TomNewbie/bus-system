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
		map.on('dblclick', (e) => {
			console.log(`A dblclick event has occurred at ${e.lngLat}`);
		});
		map.on('move', () => {
			updateData();
		});
		map.addControl(new NavigationControl());

		let a = [
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 1,
					segment_name: 'Köln Sparkasse Am Butzweilerhof - Köln IKEA Am Butzweilerhof',
					start_stop_name: 'Köln Sparkasse Am Butzweilerhof',
					end_stop_name: 'Köln IKEA Am Butzweilerhof',
					segment_id: '903 - 976',
					start_stop_id: '903',
					end_stop_id: '976',
					distance_m: 606.73861285806993
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.88748, 50.98528],
						[6.88748, 50.98528],
						[6.88973, 50.9841],
						[6.894371476770073, 50.981994066801235]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 2,
					segment_name: 'Köln IKEA Am Butzweilerhof - Köln Alter Flughafen Butzweilerhof',
					start_stop_name: 'Köln IKEA Am Butzweilerhof',
					end_stop_name: 'Köln Alter Flughafen Butzweilerhof',
					segment_id: '976 - 274',
					start_stop_id: '976',
					end_stop_id: '274',
					distance_m: 569.97960448020774
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.894371476770073, 50.981994066801235],
						[6.89524, 50.9816],
						[6.89653, 50.98081],
						[6.89701, 50.98035],
						[6.89725, 50.97951],
						[6.897520394867779, 50.97760757896598]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 3,
					segment_name: 'Köln Alter Flughafen Butzweilerhof - Köln Rektor-Klein-Str.',
					start_stop_name: 'Köln Alter Flughafen Butzweilerhof',
					end_stop_name: 'Köln Rektor-Klein-Str.',
					segment_id: '274 - 272',
					start_stop_id: '274',
					end_stop_id: '272',
					distance_m: 762.71841969297043
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.897520394867779, 50.97760757896598],
						[6.89753, 50.97754],
						[6.90192, 50.97741],
						[6.90305, 50.97729],
						[6.90326, 50.97715],
						[6.9034, 50.97699],
						[6.90386, 50.97577],
						[6.90432, 50.97494],
						[6.904636553152323, 50.974183789691672]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 4,
					segment_name: 'Köln Rektor-Klein-Str. - Köln Margaretastr.',
					start_stop_name: 'Köln Rektor-Klein-Str.',
					end_stop_name: 'Köln Margaretastr.',
					segment_id: '272 - 273',
					start_stop_id: '272',
					end_stop_id: '273',
					distance_m: 665.05552954712346
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.904636553152323, 50.974183789691672],
						[6.90468, 50.97408],
						[6.905492928787229, 50.968230878238224]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 5,
					segment_name: 'Köln Margaretastr. - Köln Iltisstr.',
					start_stop_name: 'Köln Margaretastr.',
					end_stop_name: 'Köln Iltisstr.',
					segment_id: '273 - 249',
					start_stop_id: '273',
					end_stop_id: '249',
					distance_m: 667.15990464117397
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.905492928787229, 50.968230878238224],
						[6.9055, 50.96818],
						[6.90559, 50.968],
						[6.90582, 50.96787],
						[6.90855, 50.96749],
						[6.91092, 50.96729],
						[6.91122, 50.96716],
						[6.91127, 50.96693],
						[6.91119, 50.96631],
						[6.91194, 50.96532],
						[6.912034522147954, 50.965231596473231]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 6,
					segment_name: 'Köln Iltisstr. - Köln Lenauplatz',
					start_stop_name: 'Köln Iltisstr.',
					end_stop_name: 'Köln Lenauplatz',
					segment_id: '249 - 247',
					start_stop_id: '249',
					end_stop_id: '247',
					distance_m: 867.67021757823841
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.912034522147954, 50.965231596473231],
						[6.91642, 50.96113],
						[6.9175, 50.96],
						[6.91815, 50.95906],
						[6.918352314303068, 50.958570529911931]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 7,
					segment_name: 'Köln Lenauplatz - Köln Nußbaumerstr.',
					start_stop_name: 'Köln Lenauplatz',
					end_stop_name: 'Köln Nußbaumerstr.',
					segment_id: '247 - 246',
					start_stop_id: '247',
					end_stop_id: '246',
					distance_m: 512.71689628830563
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.918352314303068, 50.958570529911931],
						[6.91846, 50.95831],
						[6.92018, 50.95805],
						[6.92403, 50.95768],
						[6.92405, 50.95747],
						[6.923579860578435, 50.957003183118516]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '100',
					route_id: '100005',
					route_name: '5',
					direction_id: 0,
					stop_sequence: 8,
					segment_name: 'Köln Nußbaumerstr. - Köln Subbelrather Str./Gürtel',
					start_stop_name: 'Köln Nußbaumerstr.',
					end_stop_name: 'Köln Subbelrather Str./Gürtel',
					segment_id: '246 - 245',
					start_stop_id: '246',
					end_stop_id: '245',
					distance_m: 307.32125350694412
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.923579860578435, 50.957003183118516],
						[6.921232049519021, 50.954671964363406]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 1,
					segment_name: 'Bergisch Gladbach (S) - Bergisch Gladbach Markt',
					start_stop_name: 'Bergisch Gladbach (S)',
					end_stop_name: 'Bergisch Gladbach Markt',
					segment_id: '5208 - 3314',
					start_stop_id: '5208',
					end_stop_id: '3314',
					distance_m: 495.55443770802947
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.124775747297698, 50.990992222685506],
						[7.12673, 50.99195],
						[7.12696, 50.99216],
						[7.12692, 50.99249],
						[7.12996, 50.99189],
						[7.130024222558013, 50.991595462061525]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 2,
					segment_name: 'Bergisch Gladbach Markt - Bergisch Gladbach Forum',
					start_stop_name: 'Bergisch Gladbach Markt',
					end_stop_name: 'Bergisch Gladbach Forum',
					segment_id: '3314 - 3305',
					start_stop_id: '3314',
					end_stop_id: '3305',
					distance_m: 396.76072372590642
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.130024222558013, 50.991595462061525],
						[7.13025, 50.99056],
						[7.13056, 50.99017],
						[7.131, 50.99019],
						[7.13184, 50.99029],
						[7.13244, 50.9905],
						[7.133451870951037, 50.991037405146244]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 3,
					segment_name: 'Bergisch Gladbach Forum - Bergisch Gladbach Sonnenweg',
					start_stop_name: 'Bergisch Gladbach Forum',
					end_stop_name: 'Bergisch Gladbach Sonnenweg',
					segment_id: '3305 - 3343',
					start_stop_id: '3305',
					end_stop_id: '3343',
					distance_m: 847.69425230180036
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.133451870951037, 50.991037405146244],
						[7.13453, 50.99161],
						[7.13616, 50.99158],
						[7.1372, 50.9917],
						[7.13915, 50.99158],
						[7.14003, 50.99164],
						[7.14224, 50.99231],
						[7.144877999500832, 50.992618337603993]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 4,
					segment_name: 'Bergisch Gladbach Sonnenweg - Bergisch Gladbach Heiligenstock',
					start_stop_name: 'Bergisch Gladbach Sonnenweg',
					end_stop_name: 'Bergisch Gladbach Heiligenstock',
					segment_id: '3343 - 6688',
					start_stop_id: '3343',
					end_stop_id: '6688',
					distance_m: 175.76593708140797
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.144877999500832, 50.992618337603993],
						[7.14686, 50.99285],
						[7.147214467055446, 50.99306190965271]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 5,
					segment_name: 'Bergisch Gladbach Heiligenstock - Bergisch Gladbach Dombach',
					start_stop_name: 'Bergisch Gladbach Heiligenstock',
					end_stop_name: 'Bergisch Gladbach Dombach',
					segment_id: '6688 - 3344',
					start_stop_id: '6688',
					end_stop_id: '3344',
					distance_m: 687.72006066222764
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.147214467055446, 50.99306190965271],
						[7.14778, 50.9934],
						[7.14816, 50.99354],
						[7.14932, 50.99373],
						[7.15282, 50.99451],
						[7.15351, 50.99459],
						[7.15394, 50.99454],
						[7.15571, 50.99409],
						[7.156319031450987, 50.994012580747757]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 6,
					segment_name: 'Bergisch Gladbach Dombach - Bergisch Gladbach Schiff',
					start_stop_name: 'Bergisch Gladbach Dombach',
					end_stop_name: 'Bergisch Gladbach Schiff',
					segment_id: '3344 - 3345',
					start_stop_id: '3344',
					end_stop_id: '3345',
					distance_m: 1847.9873649439485
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.156319031450987, 50.994012580747757],
						[7.15689, 50.99394],
						[7.1585, 50.9941],
						[7.15964, 50.9943],
						[7.16059, 50.99467],
						[7.16208, 50.99574],
						[7.16558, 50.99751],
						[7.16645, 50.99774],
						[7.16858, 50.99797],
						[7.16929, 50.99823],
						[7.16978, 50.99852],
						[7.17055, 50.99907],
						[7.17093, 50.99947],
						[7.17164, 51.00116],
						[7.17385, 51.00323],
						[7.175176607722655, 51.004043485867669]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 7,
					segment_name: 'Bergisch Gladbach Schiff - Bergisch Gladbach Herrenstrunden',
					start_stop_name: 'Bergisch Gladbach Schiff',
					end_stop_name: 'Bergisch Gladbach Herrenstrunden',
					segment_id: '3345 - 3346',
					start_stop_id: '3345',
					end_stop_id: '3346',
					distance_m: 361.39698709804622
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.175176607722655, 51.004043485867669],
						[7.17597, 51.00453],
						[7.1783, 51.00523],
						[7.17931575129534, 51.005894145077718]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 8,
					segment_name: 'Bergisch Gladbach Herrenstrunden - Bergisch Gladbach Unterthal',
					start_stop_name: 'Bergisch Gladbach Herrenstrunden',
					end_stop_name: 'Bergisch Gladbach Unterthal',
					segment_id: '3346 - 3347',
					start_stop_id: '3346',
					end_stop_id: '3347',
					distance_m: 1233.5717650395147
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.17931575129534, 51.005894145077718],
						[7.1809, 51.00693],
						[7.18121, 51.00724],
						[7.18135, 51.00762],
						[7.18165, 51.00787],
						[7.18314, 51.00843],
						[7.18624, 51.01068],
						[7.18732, 51.01115],
						[7.18905, 51.01169],
						[7.19028, 51.01185],
						[7.19117, 51.01173],
						[7.19188, 51.0115],
						[7.19248, 51.01109],
						[7.192509997771885, 51.011063700583556]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 9,
					segment_name: 'Bergisch Gladbach Unterthal - Kürten Spitze',
					start_stop_name: 'Bergisch Gladbach Unterthal',
					end_stop_name: 'Kürten Spitze',
					segment_id: '3347 - 3354',
					start_stop_id: '3347',
					end_stop_id: '3354',
					distance_m: 1069.6044729612051
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.192509997771885, 51.011063700583556],
						[7.19321, 51.01045],
						[7.19353, 51.01029],
						[7.19409, 51.01013],
						[7.1954, 51.00998],
						[7.19711, 51.00951],
						[7.19761, 51.00951],
						[7.19891, 51.00973],
						[7.20137, 51.00946],
						[7.2019, 51.00947],
						[7.20324, 51.00969],
						[7.206805957425802, 51.009753394798686]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 10,
					segment_name: 'Kürten Spitze - Kürten Dürscheid Kirche',
					start_stop_name: 'Kürten Spitze',
					end_stop_name: 'Kürten Dürscheid Kirche',
					segment_id: '3354 - 3382',
					start_stop_id: '3354',
					end_stop_id: '3382',
					distance_m: 1077.6264128257351
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.206805957425802, 51.009753394798686],
						[7.20774, 51.00977],
						[7.20822, 51.00964],
						[7.20864, 51.00942],
						[7.21023, 51.00773],
						[7.2106, 51.00748],
						[7.21076, 51.00745],
						[7.21113, 51.00752],
						[7.21159, 51.00788],
						[7.21186, 51.00796],
						[7.21374, 51.00784],
						[7.2145, 51.0079],
						[7.21507, 51.00811],
						[7.21513, 51.00819],
						[7.21511, 51.00838],
						[7.21425, 51.00884],
						[7.21421, 51.00905],
						[7.21435, 51.00923],
						[7.21459, 51.00932],
						[7.21658, 51.00957],
						[7.216846088990826, 51.009578063302747]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 11,
					segment_name: 'Kürten Dürscheid Kirche - Kürten Steeg',
					start_stop_name: 'Kürten Dürscheid Kirche',
					end_stop_name: 'Kürten Steeg',
					segment_id: '3382 - 3381',
					start_stop_id: '3382',
					end_stop_id: '3381',
					distance_m: 519.29021864669539
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.216846088990826, 51.009578063302747],
						[7.21823, 51.00962],
						[7.21849, 51.00977],
						[7.21916, 51.0104],
						[7.2199, 51.01123],
						[7.22026, 51.01137],
						[7.22114, 51.01136],
						[7.22182, 51.01153],
						[7.22254305180188, 51.0118851460321]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 12,
					segment_name: 'Kürten Steeg - Kürten Miebach',
					start_stop_name: 'Kürten Steeg',
					end_stop_name: 'Kürten Miebach',
					segment_id: '3381 - 3380',
					start_stop_id: '3381',
					end_stop_id: '3380',
					distance_m: 859.04029398547209
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.22254305180188, 51.0118851460321],
						[7.22522, 51.0132],
						[7.22702, 51.01358],
						[7.2317, 51.0136],
						[7.233942621176471, 51.013831995294119]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 13,
					segment_name: 'Kürten Miebach - Kürten Offermannsheider Str.',
					start_stop_name: 'Kürten Miebach',
					end_stop_name: 'Kürten Offermannsheider Str.',
					segment_id: '3380 - 3379',
					start_stop_id: '3380',
					end_stop_id: '3379',
					distance_m: 880.69560568969416
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.233942621176471, 51.013831995294119],
						[7.2346, 51.0139],
						[7.23538, 51.01406],
						[7.23634, 51.01444],
						[7.2373, 51.01497],
						[7.23765, 51.01521],
						[7.238, 51.01564],
						[7.2385, 51.01603],
						[7.24082, 51.01682],
						[7.24215, 51.01748],
						[7.24283, 51.01807],
						[7.243281948073021, 51.018698318052735]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 14,
					segment_name: 'Kürten Offermannsheider Str. - Kürten Biesfeld',
					start_stop_name: 'Kürten Offermannsheider Str.',
					end_stop_name: 'Kürten Biesfeld',
					segment_id: '3379 - 5075',
					start_stop_id: '3379',
					end_stop_id: '5075',
					distance_m: 302.77382008441515
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.243281948073021, 51.018698318052735],
						[7.24365, 51.01921],
						[7.24394, 51.0194],
						[7.24436, 51.01953],
						[7.246, 51.01966],
						[7.246787744488413, 51.019916016958732]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 15,
					segment_name: 'Kürten Biesfeld - Kürten Eichhof',
					start_stop_name: 'Kürten Biesfeld',
					end_stop_name: 'Kürten Eichhof',
					segment_id: '5075 - 3378',
					start_stop_id: '5075',
					end_stop_id: '3378',
					distance_m: 1375.9022177739457
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.246787744488413, 51.019916016958732],
						[7.2472, 51.02005],
						[7.2481, 51.02022],
						[7.25044, 51.02051],
						[7.25199, 51.02084],
						[7.25271, 51.02111],
						[7.25425, 51.02203],
						[7.25641, 51.02286],
						[7.25739, 51.02391],
						[7.2591, 51.02503],
						[7.262615208089425, 51.026597233833321]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 16,
					segment_name: 'Kürten Eichhof - Kürten Breibacher Weg',
					start_stop_name: 'Kürten Eichhof',
					end_stop_name: 'Kürten Breibacher Weg',
					segment_id: '3378 - 3377',
					start_stop_id: '3378',
					end_stop_id: '3377',
					distance_m: 1339.9854825833697
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.262615208089425, 51.026597233833321],
						[7.26307, 51.0268],
						[7.26342, 51.02701],
						[7.26365, 51.02725],
						[7.26344, 51.02888],
						[7.26305, 51.0301],
						[7.26271, 51.03065],
						[7.2622, 51.03107],
						[7.26175, 51.03159],
						[7.26062, 51.03438],
						[7.2594, 51.03689],
						[7.25936, 51.03717],
						[7.25943, 51.03759],
						[7.2595670486135, 51.037889190635106]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 17,
					segment_name: 'Kürten Breibacher Weg - Kürten Waldmühle',
					start_stop_name: 'Kürten Breibacher Weg',
					end_stop_name: 'Kürten Waldmühle',
					segment_id: '3377 - 3376',
					start_stop_id: '3377',
					end_stop_id: '3376',
					distance_m: 760.95844651435573
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.2595670486135, 51.037889190635106],
						[7.26085, 51.04069],
						[7.263121327028895, 51.044345949812275]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 18,
					segment_name: 'Kürten Waldmühle - Kürten Rathaus',
					start_stop_name: 'Kürten Waldmühle',
					end_stop_name: 'Kürten Rathaus',
					segment_id: '3376 - 3375',
					start_stop_id: '3376',
					end_stop_id: '3375',
					distance_m: 1093.6851764762439
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.263121327028895, 51.044345949812275],
						[7.26418, 51.04605],
						[7.2642, 51.04679],
						[7.26385, 51.04736],
						[7.26311, 51.04824],
						[7.26273, 51.04938],
						[7.26271, 51.05033],
						[7.26327, 51.05097],
						[7.26602, 51.05237],
						[7.266766846114904, 51.052711889554828]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 19,
					segment_name: 'Kürten Rathaus - Kürten Ahlenbacher Mühle',
					start_stop_name: 'Kürten Rathaus',
					end_stop_name: 'Kürten Ahlenbacher Mühle',
					segment_id: '3375 - 8282',
					start_stop_id: '3375',
					end_stop_id: '8282',
					distance_m: 338.51929058915891
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.266766846114904, 51.052711889554828],
						[7.26827, 51.0534],
						[7.271086102237768, 51.053997084968138]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 20,
					segment_name: 'Kürten Ahlenbacher Mühle - Kürten Splash Bad',
					start_stop_name: 'Kürten Ahlenbacher Mühle',
					end_stop_name: 'Kürten Splash Bad',
					segment_id: '8282 - 3394',
					start_stop_id: '8282',
					end_stop_id: '3394',
					distance_m: 1231.971211566876
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.271086102237768, 51.053997084968138],
						[7.27459, 51.05474],
						[7.27694, 51.05539],
						[7.27958, 51.0558],
						[7.28656, 51.05709],
						[7.28739, 51.05714],
						[7.287872183763692, 51.057106657505699]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 21,
					segment_name: 'Kürten Splash Bad - Kürten Sürth',
					start_stop_name: 'Kürten Splash Bad',
					end_stop_name: 'Kürten Sürth',
					segment_id: '3394 - 3393',
					start_stop_id: '3394',
					end_stop_id: '3393',
					distance_m: 737.07599590529185
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.287872183763692, 51.057106657505699],
						[7.28927, 51.05701],
						[7.29125, 51.05716],
						[7.29194, 51.05728],
						[7.29248, 51.05755],
						[7.29322, 51.05819],
						[7.29389, 51.05851],
						[7.29631, 51.05897],
						[7.297256792040547, 51.059303930802685]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 22,
					segment_name: 'Kürten Sürth - Kürten Eulensiefen',
					start_stop_name: 'Kürten Sürth',
					end_stop_name: 'Kürten Eulensiefen',
					segment_id: '3393 - 8708',
					start_stop_id: '3393',
					end_stop_id: '8708',
					distance_m: 295.50489102469902
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.297256792040547, 51.059303930802685],
						[7.29872, 51.05982],
						[7.300484736733832, 51.060970539145096]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 23,
					segment_name: 'Kürten Eulensiefen - Kürten Häcksbilstein',
					start_stop_name: 'Kürten Eulensiefen',
					end_stop_name: 'Kürten Häcksbilstein',
					segment_id: '8708 - 8709',
					start_stop_id: '8708',
					end_stop_id: '8709',
					distance_m: 784.71789649258062
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.300484736733832, 51.060970539145096],
						[7.3028, 51.06248],
						[7.30412, 51.06369],
						[7.30468, 51.06391],
						[7.3051, 51.06398],
						[7.30913, 51.06334],
						[7.309414099737333, 51.063331231489585]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 24,
					segment_name: 'Kürten Häcksbilstein - Kürten Junkermühle',
					start_stop_name: 'Kürten Häcksbilstein',
					end_stop_name: 'Kürten Junkermühle',
					segment_id: '8709 - 3392',
					start_stop_id: '8709',
					end_stop_id: '3392',
					distance_m: 737.42196419451761
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.309414099737333, 51.063331231489585],
						[7.31237, 51.06324],
						[7.31327, 51.06335],
						[7.31383, 51.06367],
						[7.31663, 51.06616],
						[7.31701, 51.06596],
						[7.31663, 51.06617],
						[7.3166596, 51.0661922]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 25,
					segment_name: 'Kürten Junkermühle - Kürten Furth',
					start_stop_name: 'Kürten Junkermühle',
					end_stop_name: 'Kürten Furth',
					segment_id: '3392 - 3395',
					start_stop_id: '3392',
					end_stop_id: '3395',
					distance_m: 1229.9339241991963
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.3166596, 51.0661922],
						[7.31683, 51.06632],
						[7.31768, 51.06667],
						[7.3205, 51.06739],
						[7.32247, 51.06875],
						[7.32686, 51.07069],
						[7.32888, 51.07179],
						[7.32961, 51.07191],
						[7.33027, 51.07182],
						[7.330918252635958, 51.071479576828047]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 26,
					segment_name: 'Kürten Furth - Wipperfürth Jörgensmühle',
					start_stop_name: 'Kürten Furth',
					end_stop_name: 'Wipperfürth Jörgensmühle',
					segment_id: '3395 - 3407',
					start_stop_id: '3395',
					end_stop_id: '3407',
					distance_m: 1181.6754213162933
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.330918252635958, 51.071479576828047],
						[7.33206, 51.07088],
						[7.33363, 51.07052],
						[7.33469, 51.0705],
						[7.33812, 51.07096],
						[7.33965, 51.07085],
						[7.3421, 51.07125],
						[7.3447, 51.0713],
						[7.346981958205629, 51.071890161604905]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 27,
					segment_name: 'Wipperfürth Jörgensmühle - Wipperfürth Ommerborn Abzw.',
					start_stop_name: 'Wipperfürth Jörgensmühle',
					end_stop_name: 'Wipperfürth Ommerborn Abzw.',
					segment_id: '3407 - 3418',
					start_stop_id: '3407',
					end_stop_id: '3418',
					distance_m: 663.61804183433162
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.346981958205629, 51.071890161604905],
						[7.3476, 51.07205],
						[7.34818, 51.07212],
						[7.34943, 51.07206],
						[7.35, 51.07222],
						[7.35056, 51.07251],
						[7.35159, 51.07208],
						[7.35256, 51.0713],
						[7.35371, 51.07072],
						[7.3539, 51.07042],
						[7.35406, 51.07031],
						[7.354450663129973, 51.070578580901852]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 28,
					segment_name: 'Wipperfürth Ommerborn Abzw. - Wipperfürth Ballsiefen',
					start_stop_name: 'Wipperfürth Ommerborn Abzw.',
					end_stop_name: 'Wipperfürth Ballsiefen',
					segment_id: '3418 - 3408',
					start_stop_id: '3418',
					end_stop_id: '3408',
					distance_m: 495.56511717703449
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.354450663129973, 51.070578580901852],
						[7.3547, 51.07075],
						[7.356, 51.07049],
						[7.35686, 51.07058],
						[7.35728, 51.07083],
						[7.3578, 51.07161],
						[7.35823, 51.07189],
						[7.359867754192757, 51.072531289292343]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 29,
					segment_name: 'Wipperfürth Ballsiefen - Wipperfürth Am Buschfelde',
					start_stop_name: 'Wipperfürth Ballsiefen',
					end_stop_name: 'Wipperfürth Am Buschfelde',
					segment_id: '3408 - 2901',
					start_stop_id: '3408',
					end_stop_id: '2901',
					distance_m: 722.41556063366659
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.359867754192757, 51.072531289292343],
						[7.35989, 51.07254],
						[7.36033, 51.07262],
						[7.36149, 51.07262],
						[7.36163, 51.07273],
						[7.3625, 51.07448],
						[7.36302, 51.07519],
						[7.36462, 51.07584],
						[7.36519, 51.07615],
						[7.366164568144446, 51.07697563950039]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 30,
					segment_name: 'Wipperfürth Am Buschfelde - Wipperfürth Thier',
					start_stop_name: 'Wipperfürth Am Buschfelde',
					end_stop_name: 'Wipperfürth Thier',
					segment_id: '2901 - 3409',
					start_stop_id: '2901',
					end_stop_id: '3409',
					distance_m: 416.77628041867831
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.366164568144446, 51.07697563950039],
						[7.36892, 51.07931],
						[7.36906, 51.07953],
						[7.369592132216612, 51.080029131769066]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 31,
					segment_name: 'Wipperfürth Thier - Wipperfürth Fürden',
					start_stop_name: 'Wipperfürth Thier',
					end_stop_name: 'Wipperfürth Fürden',
					segment_id: '3409 - 3410',
					start_stop_id: '3409',
					end_stop_id: '3410',
					distance_m: 915.50687031728887
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.369592132216612, 51.080029131769066],
						[7.37164, 51.08195],
						[7.37205, 51.08243],
						[7.37238, 51.08306],
						[7.37315, 51.08404],
						[7.37315, 51.08422],
						[7.37275, 51.08501],
						[7.372, 51.08607],
						[7.37094, 51.08695],
						[7.370667141965679, 51.087244862714506]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 32,
					segment_name: 'Wipperfürth Fürden - Wipperfürth Erlen',
					start_stop_name: 'Wipperfürth Fürden',
					end_stop_name: 'Wipperfürth Erlen',
					segment_id: '3410 - 3412',
					start_stop_id: '3410',
					end_stop_id: '3412',
					distance_m: 1199.555386568243
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.370667141965679, 51.087244862714506],
						[7.37032, 51.08762],
						[7.37014, 51.08772],
						[7.36968, 51.08779],
						[7.36968, 51.08799],
						[7.3693, 51.08899],
						[7.36929, 51.0893],
						[7.36945, 51.08974],
						[7.36997, 51.09057],
						[7.37359, 51.09588],
						[7.37369, 51.09629],
						[7.37367, 51.09659],
						[7.373601963954155, 51.097114277765044]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 33,
					segment_name: 'Wipperfürth Erlen - Wipperfürth Weinbach',
					start_stop_name: 'Wipperfürth Erlen',
					end_stop_name: 'Wipperfürth Weinbach',
					segment_id: '3412 - 3413',
					start_stop_id: '3412',
					end_stop_id: '3413',
					distance_m: 945.85918378732617
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.373601963954155, 51.097114277765044],
						[7.37333, 51.09921],
						[7.37337, 51.09987],
						[7.37353, 51.10015],
						[7.37375, 51.10035],
						[7.37452, 51.10068],
						[7.37873, 51.10109],
						[7.381631889664732, 51.101716243666246]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 34,
					segment_name: 'Wipperfürth Weinbach - Wipperfürth Unterweinbach',
					start_stop_name: 'Wipperfürth Weinbach',
					end_stop_name: 'Wipperfürth Unterweinbach',
					segment_id: '3413 - 3414',
					start_stop_id: '3413',
					end_stop_id: '3414',
					distance_m: 734.31435585006182
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.381631889664732, 51.101716243666246],
						[7.38202, 51.1018],
						[7.38253, 51.102],
						[7.38271, 51.10233],
						[7.38258, 51.10278],
						[7.38181, 51.10445],
						[7.38143, 51.10659],
						[7.38114, 51.10697],
						[7.3820207985414, 51.107608163471504]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 35,
					segment_name: 'Wipperfürth Unterweinbach - Wipperfürth Dr.-Leo-Zorn-Platz',
					start_stop_name: 'Wipperfürth Unterweinbach',
					end_stop_name: 'Wipperfürth Dr.-Leo-Zorn-Platz',
					segment_id: '3414 - 3415',
					start_stop_id: '3414',
					end_stop_id: '3415',
					distance_m: 951.44569693043468
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.3820207985414, 51.107608163471504],
						[7.38379, 51.10889],
						[7.38574, 51.11003],
						[7.3866, 51.11068],
						[7.3887, 51.11363],
						[7.389679027084017, 51.114544190853287]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 36,
					segment_name: 'Wipperfürth Dr.-Leo-Zorn-Platz - Wipperfürth Klosterplatz',
					start_stop_name: 'Wipperfürth Dr.-Leo-Zorn-Platz',
					end_stop_name: 'Wipperfürth Klosterplatz',
					segment_id: '3415 - 2626',
					start_stop_id: '3415',
					end_stop_id: '2626',
					distance_m: 533.76260777540892
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.389679027084017, 51.114544190853287],
						[7.39021, 51.11504],
						[7.3918, 51.11511],
						[7.39439, 51.11487],
						[7.39674, 51.115],
						[7.39683515947925, 51.115025790886904]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1000',
					route_id: '1100426',
					route_name: '426',
					direction_id: 0,
					stop_sequence: 37,
					segment_name: 'Wipperfürth Klosterplatz - Wipperfürth Busbf',
					start_stop_name: 'Wipperfürth Klosterplatz',
					end_stop_name: 'Wipperfürth Busbf',
					segment_id: '2626 - 3416',
					start_stop_id: '2626',
					end_stop_id: '3416',
					distance_m: 379.19635205039384
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.39683515947925, 51.115025790886904],
						[7.39888, 51.11558],
						[7.3993, 51.11601],
						[7.40012, 51.11636],
						[7.40002, 51.11674],
						[7.39972, 51.11686],
						[7.3996, 51.11712]
					]
				}
			}
		];
		// will refactor in later
		const groupedData = {};
		function getRandomColorExceptWhite() {
			let red, green, blue;
			do {
				red = Math.floor(Math.random() * 256);
				green = Math.floor(Math.random() * 256);
				blue = Math.floor(Math.random() * 256);
			} while (red === 255 && green === 255 && blue === 255); // Continue generating until not white

			return `rgb(${red}, ${green}, ${blue})`;
		}

		function getRainbowColor(index) {
			const lgbtColorsHex = ['#FF0018', '#FFA52D', '#FFFF41', '#008018', '#0000F9', '#86007D'];
			return lgbtColorsHex[index % lgbtColorsHex.length];
		}
		a.forEach((feature) => {
			const shapeId = feature.properties.shape_id;
			if (!groupedData[shapeId]) {
				groupedData[shapeId] = [];
			}
			groupedData[shapeId].push(feature);
		});

		const results = Object.values(groupedData);
		console.log('hehehe' + results);
		map.on('load', () => {
			results.forEach((result, index) => {
				map.addSource(`route ${index}`, {
					type: 'geojson',
					data: {
						type: 'FeatureCollection',
						features: result
					}
				});
				console.log('heheheh');
				const color = getRainbowColor(index);
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
			});

		map.on('click', 'route 0', (e) => {
			const routeNumber = 0;
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
		});
		map.on('mouseenter', 'route 0', () => {
			map.getCanvas().style.cursor = 'pointer';
		});
		map.on('mouseleave', 'route 0', () => {
			map.getCanvas().style.cursor = '';
		});
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
