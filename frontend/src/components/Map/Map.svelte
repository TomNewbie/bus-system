<script>
	// @ts-nocheck

	import { onMount, onDestroy } from 'svelte';
	// @ts-ignore
	import { Map, Marker, Popup } from 'mapbox-gl';
	import '../../../node_modules/mapbox-gl/dist/mapbox-gl.css';
	import createCustomMarkerForSegment from './MapMarker.svelte';

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

		map.on('move', () => {
			updateData();
		});
		let a = [
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 1,
					segment_name: 'Leverkusen Forellental - Leverkusen Schöne Aussicht',
					start_stop_name: 'Leverkusen Forellental',
					end_stop_name: 'Leverkusen Schöne Aussicht',
					segment_id: '3054 - 3055',
					start_stop_id: '3054',
					end_stop_id: '3055',
					distance_m: 518.78563875933503
				},
				geometry: {
					type: 'LineString',
					coordinates: [
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
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 2,
					segment_name: 'Leverkusen Schöne Aussicht - Leverkusen Kinderhausen',
					start_stop_name: 'Leverkusen Schöne Aussicht',
					end_stop_name: 'Leverkusen Kinderhausen',
					segment_id: '3055 - 3056',
					start_stop_id: '3055',
					end_stop_id: '3056',
					distance_m: 505.52735625100286
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.056734830056906, 51.072861874030004],
						[7.05701, 51.07234],
						[7.05708, 51.07176],
						[7.05645, 51.071],
						[7.05628, 51.07055],
						[7.0565, 51.07027],
						[7.05732, 51.06969],
						[7.057873856041132, 51.068748444730076]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 3,
					segment_name: 'Leverkusen Kinderhausen - Leverkusen Lützenkirchen Mitte',
					start_stop_name: 'Leverkusen Kinderhausen',
					end_stop_name: 'Leverkusen Lützenkirchen Mitte',
					segment_id: '3056 - 3045',
					start_stop_id: '3056',
					end_stop_id: '3045',
					distance_m: 501.50908114052606
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.057873856041132, 51.068748444730076],
						[7.05792, 51.06867],
						[7.058, 51.06841],
						[7.05834, 51.06818],
						[7.05816, 51.06799],
						[7.05801, 51.06754],
						[7.05786, 51.06648],
						[7.05792, 51.0658],
						[7.05661, 51.06557],
						[7.055843122126276, 51.065281653919477]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 4,
					segment_name: 'Leverkusen Lützenkirchen Mitte - Leverkusen Leineweberstr.',
					start_stop_name: 'Leverkusen Lützenkirchen Mitte',
					end_stop_name: 'Leverkusen Leineweberstr.',
					segment_id: '3045 - 3044',
					start_stop_id: '3045',
					end_stop_id: '3044',
					distance_m: 406.63257008094104
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.055843122126276, 51.065281653919477],
						[7.05536, 51.0651],
						[7.05308, 51.06475],
						[7.05164, 51.0644],
						[7.050290963113546, 51.064403757762918]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 5,
					segment_name: 'Leverkusen Leineweberstr. - Leverkusen In Holzhausen',
					start_stop_name: 'Leverkusen Leineweberstr.',
					end_stop_name: 'Leverkusen In Holzhausen',
					segment_id: '3044 - 3043',
					start_stop_id: '3044',
					end_stop_id: '3043',
					distance_m: 422.82332038330361
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.050290963113546, 51.064403757762918],
						[7.04805, 51.06441],
						[7.0448, 51.06387],
						[7.04440155531656, 51.06376710494439]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 6,
					segment_name: 'Leverkusen In Holzhausen - Leverkusen Feldsiefer Weg',
					start_stop_name: 'Leverkusen In Holzhausen',
					end_stop_name: 'Leverkusen Feldsiefer Weg',
					segment_id: '3043 - 3042',
					start_stop_id: '3043',
					end_stop_id: '3042',
					distance_m: 305.75995046329712
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.04440155531656, 51.06376710494439],
						[7.04298, 51.0634],
						[7.040154029419448, 51.063416148403313]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 7,
					segment_name: 'Leverkusen Feldsiefer Weg - Leverkusen In der Dasladen',
					start_stop_name: 'Leverkusen Feldsiefer Weg',
					end_stop_name: 'Leverkusen In der Dasladen',
					segment_id: '3042 - 8935',
					start_stop_id: '3042',
					end_stop_id: '8935',
					distance_m: 234.03240781302532
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.040154029419448, 51.063416148403313],
						[7.03773, 51.06343],
						[7.036831261829653, 51.063322151419555]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 8,
					segment_name: 'Leverkusen In der Dasladen - Leverkusen Holzer Weg',
					start_stop_name: 'Leverkusen In der Dasladen',
					end_stop_name: 'Leverkusen Holzer Weg',
					segment_id: '8935 - 3041',
					start_stop_id: '8935',
					end_stop_id: '3041',
					distance_m: 242.73097446701439
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.036831261829653, 51.063322151419555],
						[7.03573, 51.06319],
						[7.03357391662129, 51.062613688405058]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 9,
					segment_name: 'Leverkusen Holzer Weg - Leverkusen Jakobistr.',
					start_stop_name: 'Leverkusen Holzer Weg',
					end_stop_name: 'Leverkusen Jakobistr.',
					segment_id: '3041 - 3040',
					start_stop_id: '3041',
					end_stop_id: '3040',
					distance_m: 410.25084473340462
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.03357391662129, 51.062613688405058],
						[7.02937, 51.06149],
						[7.028202486400001, 51.061149475199997]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 10,
					segment_name: 'Leverkusen Jakobistr. - Leverkusen Quettinger Str.',
					start_stop_name: 'Leverkusen Jakobistr.',
					end_stop_name: 'Leverkusen Quettinger Str.',
					segment_id: '3040 - 3039',
					start_stop_id: '3040',
					end_stop_id: '3039',
					distance_m: 677.81154154972387
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.028202486400001, 51.061149475199997],
						[7.02577, 51.06044],
						[7.019019410354796, 51.059298356162941]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 11,
					segment_name: 'Leverkusen Quettinger Str. - Leverkusen Rathaus-Galerie',
					start_stop_name: 'Leverkusen Quettinger Str.',
					end_stop_name: 'Leverkusen Rathaus-Galerie',
					segment_id: '3039 - 1289',
					start_stop_id: '3039',
					end_stop_id: '1289',
					distance_m: 4483.6795501335655
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.019019410354796, 51.059298356162941],
						[7.01897, 51.05929],
						[7.01915, 51.05801],
						[7.01909, 51.05733],
						[7.01886, 51.05652],
						[7.01856, 51.05583],
						[7.01578, 51.0558],
						[7.01016, 51.05468],
						[7.00739, 51.05448],
						[7.0059, 51.05449],
						[7.00338, 51.05465],
						[6.99938, 51.05516],
						[6.99886, 51.05507],
						[6.9988, 51.0549],
						[6.99897, 51.05476],
						[7.00009, 51.05461],
						[7.00033, 51.05452],
						[6.99916, 51.05287],
						[6.99918, 51.0528],
						[6.99899, 51.05253],
						[6.99481, 51.0471],
						[6.99121, 51.04134],
						[6.99063, 51.0407],
						[6.9884, 51.03885],
						[6.98769, 51.03792],
						[6.9875, 51.03751],
						[6.98738, 51.03622],
						[6.98745, 51.03573],
						[6.98782, 51.03496],
						[6.988671568351731, 51.033727806400151]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1',
					route_id: '300020',
					route_name: 'SB20',
					direction_id: 0,
					stop_sequence: 12,
					segment_name: 'Leverkusen Rathaus-Galerie - Leverkusen Mitte Bf',
					start_stop_name: 'Leverkusen Rathaus-Galerie',
					end_stop_name: 'Leverkusen Mitte Bf',
					segment_id: '1289 - 5228',
					start_stop_id: '1289',
					end_stop_id: '5228',
					distance_m: 291.58273997126639
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.988671568351731, 51.033727806400151],
						[6.98914, 51.03305],
						[6.99033, 51.03324],
						[6.99048, 51.03299],
						[6.99019, 51.03291],
						[6.99025, 51.03227]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 1,
					segment_name: 'Euskirchen Oberwichterich - Euskirchen Frauenberg Kirche',
					start_stop_name: 'Euskirchen Oberwichterich',
					end_stop_name: 'Euskirchen Frauenberg Kirche',
					segment_id: '6351 - 6349',
					start_stop_id: '6351',
					end_stop_id: '6349',
					distance_m: 1131.5157044137165
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.743387280906441, 50.691563104105903],
						[6.74257, 50.69112],
						[6.74201, 50.69066],
						[6.74009, 50.68731],
						[6.73914, 50.68737],
						[6.73794, 50.68724],
						[6.73732, 50.68626],
						[6.73716, 50.68576],
						[6.73698, 50.68561],
						[6.73633, 50.68468],
						[6.737999890136146, 50.684138770785914]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 2,
					segment_name: 'Euskirchen Frauenberg Kirche - Euskirchen Mercator-Kaserne',
					start_stop_name: 'Euskirchen Frauenberg Kirche',
					end_stop_name: 'Euskirchen Mercator-Kaserne',
					segment_id: '6349 - 6348',
					start_stop_id: '6349',
					end_stop_id: '6348',
					distance_m: 2690.3653431814128
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.737999890136146, 50.684138770785914],
						[6.73886, 50.68386],
						[6.73931, 50.68463],
						[6.7399, 50.68604],
						[6.74005, 50.68688],
						[6.74111, 50.68684],
						[6.74143, 50.68712],
						[6.74189, 50.68793],
						[6.7429, 50.68769],
						[6.74451, 50.68708],
						[6.74537, 50.68667],
						[6.74644, 50.68598],
						[6.74751, 50.68516],
						[6.74897, 50.68387],
						[6.75053, 50.68234],
						[6.75226, 50.68102],
						[6.75457, 50.67985],
						[6.7568, 50.67903],
						[6.75861, 50.67825],
						[6.76085, 50.67712],
						[6.76333154705465, 50.675698531298792]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 3,
					segment_name: 'Euskirchen Mercator-Kaserne - Euskirchen Friedhof',
					start_stop_name: 'Euskirchen Mercator-Kaserne',
					end_stop_name: 'Euskirchen Friedhof',
					segment_id: '6348 - 6347',
					start_stop_id: '6348',
					end_stop_id: '6347',
					distance_m: 1116.2735274516397
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.76333154705465, 50.675698531298792],
						[6.766, 50.67417],
						[6.76752, 50.67315],
						[6.76924, 50.67185],
						[6.77357, 50.66901],
						[6.774208662012279, 50.668445702742581]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 4,
					segment_name: 'Euskirchen Friedhof - Euskirchen Jülicher Ring/Friedhof',
					start_stop_name: 'Euskirchen Friedhof',
					end_stop_name: 'Euskirchen Jülicher Ring/Friedhof',
					segment_id: '6347 - 8651',
					start_stop_id: '6347',
					end_stop_id: '8651',
					distance_m: 416.35677832709689
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.774208662012279, 50.668445702742581],
						[6.77503, 50.66772],
						[6.77689, 50.66664],
						[6.778200684117904, 50.667569394192697]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 5,
					segment_name: 'Euskirchen Jülicher Ring/Friedhof - Euskirchen Jülicher Ring/Kreishaus',
					start_stop_name: 'Euskirchen Jülicher Ring/Friedhof',
					end_stop_name: 'Euskirchen Jülicher Ring/Kreishaus',
					segment_id: '8651 - 5893',
					start_stop_id: '8651',
					end_stop_id: '5893',
					distance_m: 398.52543756298746
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.778200684117904, 50.667569394192697],
						[6.77854, 50.66781],
						[6.77904, 50.66808],
						[6.77982, 50.66835],
						[6.78116, 50.66866],
						[6.78228, 50.66881],
						[6.78297, 50.66878],
						[6.783288508220641, 50.668746997943401]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 6,
					segment_name: 'Euskirchen Jülicher Ring/Kreishaus - Euskirchen Schillingstr.',
					start_stop_name: 'Euskirchen Jülicher Ring/Kreishaus',
					end_stop_name: 'Euskirchen Schillingstr.',
					segment_id: '5893 - 8884',
					start_stop_id: '5893',
					end_stop_id: '8884',
					distance_m: 477.0690317791217
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.783288508220641, 50.668746997943401],
						[6.78712, 50.66835],
						[6.787, 50.66784],
						[6.78704, 50.66744],
						[6.787382585286782, 50.666561194264339]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 7,
					segment_name: 'Euskirchen Schillingstr. - Euskirchen Mühlenstr.',
					start_stop_name: 'Euskirchen Schillingstr.',
					end_stop_name: 'Euskirchen Mühlenstr.',
					segment_id: '8884 - 8786',
					start_stop_id: '8884',
					end_stop_id: '8786',
					distance_m: 306.61167819386236
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.787382585286782, 50.666561194264339],
						[6.78773, 50.66567],
						[6.78836, 50.66446],
						[6.788517367010308, 50.663905074226804]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 8,
					segment_name: 'Euskirchen Mühlenstr. - Euskirchen Evangelische Kirche',
					start_stop_name: 'Euskirchen Mühlenstr.',
					end_stop_name: 'Euskirchen Evangelische Kirche',
					segment_id: '8786 - 7008',
					start_stop_id: '8786',
					end_stop_id: '7008',
					distance_m: 789.80473919143492
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.788517367010308, 50.663905074226804],
						[6.78874, 50.66312],
						[6.79033, 50.66286],
						[6.79008, 50.66241],
						[6.78954, 50.66209],
						[6.79054, 50.66137],
						[6.79154, 50.66114],
						[6.79192, 50.66088],
						[6.79194, 50.66081],
						[6.79121, 50.66017],
						[6.793491891293195, 50.660336489922678]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '10',
					route_id: '2200865',
					route_name: '865',
					direction_id: 1,
					stop_sequence: 9,
					segment_name: 'Euskirchen Evangelische Kirche - Euskirchen Bf',
					start_stop_name: 'Euskirchen Evangelische Kirche',
					end_stop_name: 'Euskirchen Bf',
					segment_id: '7008 - 6058',
					start_stop_id: '7008',
					end_stop_id: '6058',
					distance_m: 552.48584820491544
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.793491891293195, 50.660336489922678],
						[6.79587, 50.66051],
						[6.79571, 50.66023],
						[6.79449, 50.65881],
						[6.79282, 50.65841],
						[6.7922, 50.65838]
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
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 1,
					segment_name: 'Leverkusen Stegerwaldstr. - Leverkusen Legienstr.',
					start_stop_name: 'Leverkusen Stegerwaldstr.',
					end_stop_name: 'Leverkusen Legienstr.',
					segment_id: '3219 - 3218',
					start_stop_id: '3219',
					end_stop_id: '3218',
					distance_m: 234.66507532567064
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.00636, 51.02916],
						[7.00636, 51.02916],
						[7.00715, 51.02798],
						[7.007917587053956, 51.027307176779864]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 2,
					segment_name: 'Leverkusen Legienstr. - Leverkusen Heinrich-Heine-Str.',
					start_stop_name: 'Leverkusen Legienstr.',
					end_stop_name: 'Leverkusen Heinrich-Heine-Str.',
					segment_id: '3218 - 3217',
					start_stop_id: '3218',
					end_stop_id: '3217',
					distance_m: 300.60750275671523
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.007917587053956, 51.027307176779864],
						[7.00796, 51.02727],
						[7.00864, 51.02649],
						[7.00902, 51.02587],
						[7.00916, 51.02535],
						[7.0084, 51.02512],
						[7.00833542320819, 51.025106597269627]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 3,
					segment_name: 'Leverkusen Heinrich-Heine-Str. - Leverkusen Karl-Krekeler Str.',
					start_stop_name: 'Leverkusen Heinrich-Heine-Str.',
					end_stop_name: 'Leverkusen Karl-Krekeler Str.',
					segment_id: '3217 - 4054',
					start_stop_id: '3217',
					end_stop_id: '4054',
					distance_m: 301.01816175294215
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.00833542320819, 51.025106597269627],
						[7.004259361433448, 51.0242606221843]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 4,
					segment_name: 'Leverkusen Karl-Krekeler Str. - Leverkusen Leipziger Str.',
					start_stop_name: 'Leverkusen Karl-Krekeler Str.',
					end_stop_name: 'Leverkusen Leipziger Str.',
					segment_id: '4054 - 4053',
					start_stop_id: '4054',
					end_stop_id: '4053',
					distance_m: 378.45875625705219
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.004259361433448, 51.0242606221843],
						[7.00363, 51.02413],
						[7.00307, 51.02517],
						[7.002404314730001, 51.027008955558372]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 5,
					segment_name: 'Leverkusen Leipziger Str. - Leverkusen Jenaer Str.',
					start_stop_name: 'Leverkusen Leipziger Str.',
					end_stop_name: 'Leverkusen Jenaer Str.',
					segment_id: '4053 - 3215',
					start_stop_id: '4053',
					end_stop_id: '3215',
					distance_m: 271.19581115853015
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.002404314730001, 51.027008955558372],
						[7.00227, 51.02738],
						[7.00212, 51.02751],
						[7.00193, 51.02753],
						[6.999311828574479, 51.026877660991616]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 6,
					segment_name: 'Leverkusen Jenaer Str. - Leverkusen Zeppelinstr.',
					start_stop_name: 'Leverkusen Jenaer Str.',
					end_stop_name: 'Leverkusen Zeppelinstr.',
					segment_id: '3215 - 7677',
					start_stop_id: '3215',
					end_stop_id: '7677',
					distance_m: 381.25085911092742
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.999311828574479, 51.026877660991616],
						[6.99896, 51.02679],
						[6.99868, 51.02738],
						[6.99844, 51.0283],
						[6.9984, 51.02914],
						[6.997205794131539, 51.028868882992022]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 7,
					segment_name: 'Leverkusen Zeppelinstr. - Leverkusen Europaring',
					start_stop_name: 'Leverkusen Zeppelinstr.',
					end_stop_name: 'Leverkusen Europaring',
					segment_id: '7677 - 2545',
					start_stop_id: '7677',
					end_stop_id: '2545',
					distance_m: 627.7945381387467
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.997205794131539, 51.028868882992022],
						[6.9947, 51.0283],
						[6.99301, 51.02812],
						[6.99288, 51.02804],
						[6.99287, 51.02779],
						[6.99325, 51.02735],
						[6.99318, 51.02723],
						[6.99296, 51.02713],
						[6.99122, 51.02696],
						[6.99098, 51.02699],
						[6.99069, 51.02717],
						[6.990646224616516, 51.027365994330594]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 8,
					segment_name: 'Leverkusen Europaring - Leverkusen Mitte Bf',
					start_stop_name: 'Leverkusen Europaring',
					end_stop_name: 'Leverkusen Mitte Bf',
					segment_id: '2545 - 5228',
					start_stop_id: '2545',
					end_stop_id: '5228',
					distance_m: 885.89063886022893
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.990646224616516, 51.027365994330594],
						[6.99025, 51.02914],
						[6.98991, 51.02989],
						[6.98947, 51.0321],
						[6.98914, 51.03305],
						[6.98914, 51.03305],
						[6.99033, 51.03324],
						[6.99033, 51.03324],
						[6.99076, 51.03227],
						[6.99082, 51.03186]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 9,
					segment_name: 'Leverkusen Mitte Bf - Leverkusen Rathaus-Galerie',
					start_stop_name: 'Leverkusen Mitte Bf',
					end_stop_name: 'Leverkusen Rathaus-Galerie',
					segment_id: '5228 - 1289',
					start_stop_id: '5228',
					end_stop_id: '1289',
					distance_m: 329.04472445737895
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.99082, 51.03186],
						[6.99082, 51.03186],
						[6.99068, 51.03178],
						[6.99046, 51.0318],
						[6.99024, 51.03228],
						[6.99017, 51.03274],
						[6.99021, 51.03294],
						[6.99048, 51.03299],
						[6.988671963649096, 51.033728099909972]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 10,
					segment_name: 'Leverkusen Rathaus-Galerie - Leverkusen Am Neuenhof',
					start_stop_name: 'Leverkusen Rathaus-Galerie',
					end_stop_name: 'Leverkusen Am Neuenhof',
					segment_id: '1289 - 5227',
					start_stop_id: '1289',
					end_stop_id: '5227',
					distance_m: 912.8427996495443
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.988671963649096, 51.033728099909972],
						[6.98787, 51.03489],
						[6.98746, 51.03574],
						[6.98738, 51.03622],
						[6.98746, 51.03737],
						[6.98758, 51.03769],
						[6.98801, 51.03838],
						[6.98841, 51.03885],
						[6.99109, 51.0411]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 11,
					segment_name: 'Leverkusen Am Neuenhof - Leverkusen Tannenbergstr.',
					start_stop_name: 'Leverkusen Am Neuenhof',
					end_stop_name: 'Leverkusen Tannenbergstr.',
					segment_id: '5227 - 3153',
					start_stop_id: '5227',
					end_stop_id: '3153',
					distance_m: 433.36351671115369
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.99109, 51.0411],
						[6.99109, 51.0411],
						[6.99416, 51.03925],
						[6.99584, 51.03983],
						[6.995848129113568, 51.039839785044109]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 12,
					segment_name: 'Leverkusen Tannenbergstr. - Leverkusen Friedrich-Naumann-Str.',
					start_stop_name: 'Leverkusen Tannenbergstr.',
					end_stop_name: 'Leverkusen Friedrich-Naumann-Str.',
					segment_id: '3153 - 3154',
					start_stop_id: '3153',
					end_stop_id: '3154',
					distance_m: 273.04142554668522
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.995848129113568, 51.039839785044109],
						[6.99638, 51.04048],
						[6.99703, 51.04151],
						[6.997307815320042, 51.042108371458554]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 13,
					segment_name: 'Leverkusen Friedrich-Naumann-Str. - Leverkusen Bebelstr.',
					start_stop_name: 'Leverkusen Friedrich-Naumann-Str.',
					end_stop_name: 'Leverkusen Bebelstr.',
					segment_id: '3154 - 3155',
					start_stop_id: '3154',
					end_stop_id: '3155',
					distance_m: 235.59249309181001
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.997307815320042, 51.042108371458554],
						[6.99781, 51.04319],
						[6.998415780572395, 51.044104495671789]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 14,
					segment_name: 'Leverkusen Bebelstr. - Leverkusen Küppersteger Str.',
					start_stop_name: 'Leverkusen Bebelstr.',
					end_stop_name: 'Leverkusen Küppersteger Str.',
					segment_id: '3155 - 5226',
					start_stop_id: '3155',
					end_stop_id: '5226',
					distance_m: 443.59244347828206
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.998415780572395, 51.044104495671789],
						[6.99885, 51.04476],
						[6.99532, 51.04604],
						[6.994236984, 51.046236912]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 15,
					segment_name: 'Leverkusen Küppersteger Str. - Leverkusen Küppersteg Post',
					start_stop_name: 'Leverkusen Küppersteger Str.',
					end_stop_name: 'Leverkusen Küppersteg Post',
					segment_id: '5226 - 3210',
					start_stop_id: '5226',
					end_stop_id: '3210',
					distance_m: 272.28686545211872
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.994236984, 51.046236912],
						[6.994, 51.04628],
						[6.99103, 51.04636],
						[6.991007788520109, 51.046778316204609]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 16,
					segment_name: 'Leverkusen Küppersteg Post - Leverkusen Gisbert-Cremer-Str.',
					start_stop_name: 'Leverkusen Küppersteg Post',
					end_stop_name: 'Leverkusen Gisbert-Cremer-Str.',
					segment_id: '3210 - 3211',
					start_stop_id: '3210',
					end_stop_id: '3211',
					distance_m: 373.14122703916678
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.991007788520109, 51.046778316204609],
						[6.99091, 51.04862],
						[6.99049, 51.04927],
						[6.989646217628706, 51.049881014820592]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 17,
					segment_name: 'Leverkusen Gisbert-Cremer-Str. - Leverkusen Mühlenweg',
					start_stop_name: 'Leverkusen Gisbert-Cremer-Str.',
					end_stop_name: 'Leverkusen Mühlenweg',
					segment_id: '3211 - 3212',
					start_stop_id: '3211',
					end_stop_id: '3212',
					distance_m: 528.65793837033232
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.989646217628706, 51.049881014820592],
						[6.98962, 51.0499],
						[6.99125, 51.05198],
						[6.99222, 51.0534],
						[6.990854253646266, 51.053438904318924]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 18,
					segment_name: 'Leverkusen Mühlenweg - Leverkusen Waldstr.',
					start_stop_name: 'Leverkusen Mühlenweg',
					end_stop_name: 'Leverkusen Waldstr.',
					segment_id: '3212 - 7664',
					start_stop_id: '3212',
					end_stop_id: '7664',
					distance_m: 303.08477348949759
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.990854253646266, 51.053438904318924],
						[6.986535425275687, 51.053561929414933]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1001',
					route_id: '300204',
					route_name: '204',
					direction_id: 1,
					stop_sequence: 19,
					segment_name: 'Leverkusen Waldstr. - Leverkusen Reuschenberg Friedhof',
					start_stop_name: 'Leverkusen Waldstr.',
					end_stop_name: 'Leverkusen Reuschenberg Friedhof',
					segment_id: '7664 - 3213',
					start_stop_id: '7664',
					end_stop_id: '3213',
					distance_m: 188.57162851944003
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[6.986535425275687, 51.053561929414933],
						[6.98555, 51.05359],
						[6.98482, 51.05456]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 1,
					segment_name: 'Kürten Ahlenbacher Mühle - Kürten Rathaus',
					start_stop_name: 'Kürten Ahlenbacher Mühle',
					end_stop_name: 'Kürten Rathaus',
					segment_id: '8282 - 3375',
					start_stop_id: '8282',
					end_stop_id: '3375',
					distance_m: 339.39898766691164
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.27108, 51.05401],
						[7.27108, 51.05401],
						[7.26875, 51.05355],
						[7.26802, 51.0533],
						[7.266772219986473, 51.052700380313865]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 2,
					segment_name: 'Kürten Rathaus - Kürten Waldmühle',
					start_stop_name: 'Kürten Rathaus',
					end_stop_name: 'Kürten Waldmühle',
					segment_id: '3375 - 3376',
					start_stop_id: '3375',
					end_stop_id: '3376',
					distance_m: 1093.8391149961431
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.266772219986473, 51.052700380313865],
						[7.26365, 51.0512],
						[7.26317, 51.0509],
						[7.26271, 51.05033],
						[7.2627, 51.04961],
						[7.26287, 51.04881],
						[7.26311, 51.04824],
						[7.26385, 51.04736],
						[7.2642, 51.04679],
						[7.26418, 51.04605],
						[7.263121327028895, 51.044345949812275]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 3,
					segment_name: 'Kürten Waldmühle - Kürten Breibacher Weg',
					start_stop_name: 'Kürten Waldmühle',
					end_stop_name: 'Kürten Breibacher Weg',
					segment_id: '3376 - 3377',
					start_stop_id: '3376',
					end_stop_id: '3377',
					distance_m: 760.95844651435573
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.263121327028895, 51.044345949812275],
						[7.26085, 51.04069],
						[7.2595670486135, 51.037889190635106]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 4,
					segment_name: 'Kürten Breibacher Weg - Kürten Eichhof',
					start_stop_name: 'Kürten Breibacher Weg',
					end_stop_name: 'Kürten Eichhof',
					segment_id: '3377 - 3378',
					start_stop_id: '3377',
					end_stop_id: '3378',
					distance_m: 1339.9854825833697
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.2595670486135, 51.037889190635106],
						[7.25943, 51.03759],
						[7.25936, 51.03717],
						[7.2594, 51.03689],
						[7.26062, 51.03438],
						[7.26175, 51.03159],
						[7.2622, 51.03107],
						[7.26271, 51.03065],
						[7.26305, 51.0301],
						[7.26344, 51.02888],
						[7.26365, 51.02725],
						[7.26342, 51.02701],
						[7.26307, 51.0268],
						[7.262615208089425, 51.026597233833321]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 5,
					segment_name: 'Kürten Eichhof - Kürten Biesfeld',
					start_stop_name: 'Kürten Eichhof',
					end_stop_name: 'Kürten Biesfeld',
					segment_id: '3378 - 5075',
					start_stop_id: '3378',
					end_stop_id: '5075',
					distance_m: 1375.6961128069688
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.262615208089425, 51.026597233833321],
						[7.2591, 51.02503],
						[7.25739, 51.02391],
						[7.25641, 51.02286],
						[7.25425, 51.02203],
						[7.253, 51.02124],
						[7.25239, 51.02097],
						[7.25044, 51.02051],
						[7.24732, 51.02009],
						[7.246785062017566, 51.01992887410168]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 6,
					segment_name: 'Kürten Biesfeld - Kürten Miebach',
					start_stop_name: 'Kürten Biesfeld',
					end_stop_name: 'Kürten Miebach',
					segment_id: '5075 - 3380',
					start_stop_id: '5075',
					end_stop_id: '3380',
					distance_m: 1184.2530050574051
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.246785062017566, 51.01992887410168],
						[7.24566, 51.01959],
						[7.24436, 51.01953],
						[7.24394, 51.0194],
						[7.24365, 51.01921],
						[7.24283, 51.01807],
						[7.24215, 51.01748],
						[7.24082, 51.01682],
						[7.2385, 51.01603],
						[7.238, 51.01564],
						[7.23765, 51.01521],
						[7.2373, 51.01497],
						[7.23634, 51.01444],
						[7.23538, 51.01406],
						[7.2346, 51.0139],
						[7.233942621176471, 51.013831995294119]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 7,
					segment_name: 'Kürten Miebach - Kürten Steeg',
					start_stop_name: 'Kürten Miebach',
					end_stop_name: 'Kürten Steeg',
					segment_id: '3380 - 3381',
					start_stop_id: '3380',
					end_stop_id: '3381',
					distance_m: 859.04029398547209
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.233942621176471, 51.013831995294119],
						[7.2317, 51.0136],
						[7.22702, 51.01358],
						[7.22522, 51.0132],
						[7.22254305180188, 51.0118851460321]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 8,
					segment_name: 'Kürten Steeg - Kürten Dürscheid Kirche',
					start_stop_name: 'Kürten Steeg',
					end_stop_name: 'Kürten Dürscheid Kirche',
					segment_id: '3381 - 3382',
					start_stop_id: '3381',
					end_stop_id: '3382',
					distance_m: 519.29021864669539
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.22254305180188, 51.0118851460321],
						[7.22182, 51.01153],
						[7.22114, 51.01136],
						[7.22026, 51.01137],
						[7.2199, 51.01123],
						[7.21916, 51.0104],
						[7.21849, 51.00977],
						[7.21823, 51.00962],
						[7.216846088990826, 51.009578063302747]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 9,
					segment_name: 'Kürten Dürscheid Kirche - Kürten Spitze',
					start_stop_name: 'Kürten Dürscheid Kirche',
					end_stop_name: 'Kürten Spitze',
					segment_id: '3382 - 3354',
					start_stop_id: '3382',
					end_stop_id: '3354',
					distance_m: 1077.6264128257351
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.216846088990826, 51.009578063302747],
						[7.21658, 51.00957],
						[7.21459, 51.00932],
						[7.21435, 51.00923],
						[7.21421, 51.00905],
						[7.21425, 51.00884],
						[7.21511, 51.00838],
						[7.21513, 51.00819],
						[7.21507, 51.00811],
						[7.2145, 51.0079],
						[7.21374, 51.00784],
						[7.21186, 51.00796],
						[7.21159, 51.00788],
						[7.21113, 51.00752],
						[7.21076, 51.00745],
						[7.2106, 51.00748],
						[7.21023, 51.00773],
						[7.20864, 51.00942],
						[7.20822, 51.00964],
						[7.20774, 51.00977],
						[7.206805957425802, 51.009753394798686]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 10,
					segment_name: 'Kürten Spitze - Bergisch Gladbach Unterthal',
					start_stop_name: 'Kürten Spitze',
					end_stop_name: 'Bergisch Gladbach Unterthal',
					segment_id: '3354 - 3347',
					start_stop_id: '3354',
					end_stop_id: '3347',
					distance_m: 1069.6044729612051
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.206805957425802, 51.009753394798686],
						[7.20324, 51.00969],
						[7.2019, 51.00947],
						[7.20137, 51.00946],
						[7.19891, 51.00973],
						[7.19761, 51.00951],
						[7.19711, 51.00951],
						[7.1954, 51.00998],
						[7.19409, 51.01013],
						[7.19353, 51.01029],
						[7.19321, 51.01045],
						[7.192509997771885, 51.011063700583556]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 11,
					segment_name: 'Bergisch Gladbach Unterthal - Bergisch Gladbach Herrenstrunden',
					start_stop_name: 'Bergisch Gladbach Unterthal',
					end_stop_name: 'Bergisch Gladbach Herrenstrunden',
					segment_id: '3347 - 3346',
					start_stop_id: '3347',
					end_stop_id: '3346',
					distance_m: 1233.5717650395152
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.192509997771885, 51.011063700583556],
						[7.19248, 51.01109],
						[7.19188, 51.0115],
						[7.19117, 51.01173],
						[7.19028, 51.01185],
						[7.18905, 51.01169],
						[7.18732, 51.01115],
						[7.18624, 51.01068],
						[7.18314, 51.00843],
						[7.18165, 51.00787],
						[7.18135, 51.00762],
						[7.18121, 51.00724],
						[7.1809, 51.00693],
						[7.17931575129534, 51.005894145077718]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 12,
					segment_name: 'Bergisch Gladbach Herrenstrunden - Bergisch Gladbach Schiff',
					start_stop_name: 'Bergisch Gladbach Herrenstrunden',
					end_stop_name: 'Bergisch Gladbach Schiff',
					segment_id: '3346 - 3345',
					start_stop_id: '3346',
					end_stop_id: '3345',
					distance_m: 361.39698709804622
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.17931575129534, 51.005894145077718],
						[7.1783, 51.00523],
						[7.17597, 51.00453],
						[7.175176607722655, 51.004043485867669]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 13,
					segment_name: 'Bergisch Gladbach Schiff - Bergisch Gladbach Dombach',
					start_stop_name: 'Bergisch Gladbach Schiff',
					end_stop_name: 'Bergisch Gladbach Dombach',
					segment_id: '3345 - 3344',
					start_stop_id: '3345',
					end_stop_id: '3344',
					distance_m: 1847.9873649439483
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.175176607722655, 51.004043485867669],
						[7.17385, 51.00323],
						[7.17164, 51.00116],
						[7.17093, 50.99947],
						[7.17055, 50.99907],
						[7.16978, 50.99852],
						[7.16929, 50.99823],
						[7.16858, 50.99797],
						[7.16645, 50.99774],
						[7.16558, 50.99751],
						[7.16208, 50.99574],
						[7.16059, 50.99467],
						[7.15964, 50.9943],
						[7.1585, 50.9941],
						[7.15689, 50.99394],
						[7.156319031450987, 50.994012580747757]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 14,
					segment_name: 'Bergisch Gladbach Dombach - Bergisch Gladbach Heiligenstock',
					start_stop_name: 'Bergisch Gladbach Dombach',
					end_stop_name: 'Bergisch Gladbach Heiligenstock',
					segment_id: '3344 - 6688',
					start_stop_id: '3344',
					end_stop_id: '6688',
					distance_m: 687.72006066222752
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.156319031450987, 50.994012580747757],
						[7.15571, 50.99409],
						[7.15394, 50.99454],
						[7.15351, 50.99459],
						[7.15282, 50.99451],
						[7.14932, 50.99373],
						[7.14816, 50.99354],
						[7.14778, 50.9934],
						[7.147214467055446, 50.99306190965271]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 15,
					segment_name: 'Bergisch Gladbach Heiligenstock - Bergisch Gladbach Sonnenweg',
					start_stop_name: 'Bergisch Gladbach Heiligenstock',
					end_stop_name: 'Bergisch Gladbach Sonnenweg',
					segment_id: '6688 - 3343',
					start_stop_id: '6688',
					end_stop_id: '3343',
					distance_m: 175.76593708140797
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.147214467055446, 50.99306190965271],
						[7.14686, 50.99285],
						[7.144877999500832, 50.992618337603993]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 16,
					segment_name: 'Bergisch Gladbach Sonnenweg - Bergisch Gladbach Forum',
					start_stop_name: 'Bergisch Gladbach Sonnenweg',
					end_stop_name: 'Bergisch Gladbach Forum',
					segment_id: '3343 - 3305',
					start_stop_id: '3343',
					end_stop_id: '3305',
					distance_m: 847.69425230180047
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.144877999500832, 50.992618337603993],
						[7.14224, 50.99231],
						[7.14003, 50.99164],
						[7.13915, 50.99158],
						[7.1372, 50.9917],
						[7.13616, 50.99158],
						[7.13453, 50.99161],
						[7.133451870951037, 50.991037405146244]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 17,
					segment_name: 'Bergisch Gladbach Forum - Bergisch Gladbach Markt',
					start_stop_name: 'Bergisch Gladbach Forum',
					end_stop_name: 'Bergisch Gladbach Markt',
					segment_id: '3305 - 3314',
					start_stop_id: '3305',
					end_stop_id: '3314',
					distance_m: 396.76072372590636
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.133451870951037, 50.991037405146244],
						[7.13244, 50.9905],
						[7.13184, 50.99029],
						[7.131, 50.99019],
						[7.13056, 50.99017],
						[7.13025, 50.99056],
						[7.130024222558013, 50.991595462061525]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1002',
					route_id: '300426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 18,
					segment_name: 'Bergisch Gladbach Markt - Bergisch Gladbach (S)',
					start_stop_name: 'Bergisch Gladbach Markt',
					end_stop_name: 'Bergisch Gladbach (S)',
					segment_id: '3314 - 5208',
					start_stop_id: '3314',
					end_stop_id: '5208',
					distance_m: 495.55443770802941
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.130024222558013, 50.991595462061525],
						[7.12996, 50.99189],
						[7.12692, 50.99249],
						[7.12696, 50.99216],
						[7.12673, 50.99195],
						[7.124775747297698, 50.990992222685506]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 1,
					segment_name: 'Kürten Splash Bad/Wende - Kürten Splash Bad',
					start_stop_name: 'Kürten Splash Bad/Wende',
					end_stop_name: 'Kürten Splash Bad',
					segment_id: '7660 - 3394',
					start_stop_id: '7660',
					end_stop_id: '3394',
					distance_m: 136.39863260552931
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.28855, 51.05638],
						[7.28855, 51.05638],
						[7.28876, 51.05703],
						[7.287870786995924, 51.057084040569308]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 2,
					segment_name: 'Kürten Splash Bad - Kürten Ahlenbacher Mühle',
					start_stop_name: 'Kürten Splash Bad',
					end_stop_name: 'Kürten Ahlenbacher Mühle',
					segment_id: '3394 - 8282',
					start_stop_id: '3394',
					end_stop_id: '8282',
					distance_m: 1232.0613708798583
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.287870786995924, 51.057084040569308],
						[7.28695, 51.05714],
						[7.27694, 51.05539],
						[7.27459, 51.05474],
						[7.271086102237768, 51.053997084968138]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 3,
					segment_name: 'Kürten Ahlenbacher Mühle - Kürten Rathaus',
					start_stop_name: 'Kürten Ahlenbacher Mühle',
					end_stop_name: 'Kürten Rathaus',
					segment_id: '8282 - 3375',
					start_stop_id: '8282',
					end_stop_id: '3375',
					distance_m: 339.18906470008437
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.271086102237768, 51.053997084968138],
						[7.26827, 51.0534],
						[7.266774704320712, 51.052695021888177]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 4,
					segment_name: 'Kürten Rathaus - Kürten Waldmühle',
					start_stop_name: 'Kürten Rathaus',
					end_stop_name: 'Kürten Waldmühle',
					segment_id: '3375 - 3376',
					start_stop_id: '3375',
					end_stop_id: '3376',
					distance_m: 1093.2996865095788
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.266774704320712, 51.052695021888177],
						[7.26424, 51.0515],
						[7.26317, 51.0509],
						[7.26271, 51.05033],
						[7.26273, 51.04938],
						[7.26311, 51.04824],
						[7.26385, 51.04736],
						[7.2642, 51.04679],
						[7.26418, 51.04605],
						[7.263121327028895, 51.044345949812275]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 5,
					segment_name: 'Kürten Waldmühle - Kürten Breibacher Weg',
					start_stop_name: 'Kürten Waldmühle',
					end_stop_name: 'Kürten Breibacher Weg',
					segment_id: '3376 - 3377',
					start_stop_id: '3376',
					end_stop_id: '3377',
					distance_m: 760.95844651435573
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.263121327028895, 51.044345949812275],
						[7.26085, 51.04069],
						[7.2595670486135, 51.037889190635106]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 6,
					segment_name: 'Kürten Breibacher Weg - Kürten Eichhof',
					start_stop_name: 'Kürten Breibacher Weg',
					end_stop_name: 'Kürten Eichhof',
					segment_id: '3377 - 3378',
					start_stop_id: '3377',
					end_stop_id: '3378',
					distance_m: 1339.9854825833697
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.2595670486135, 51.037889190635106],
						[7.25943, 51.03759],
						[7.25936, 51.03717],
						[7.2594, 51.03689],
						[7.26062, 51.03438],
						[7.26175, 51.03159],
						[7.2622, 51.03107],
						[7.26271, 51.03065],
						[7.26305, 51.0301],
						[7.26344, 51.02888],
						[7.26365, 51.02725],
						[7.26342, 51.02701],
						[7.26307, 51.0268],
						[7.262615208089425, 51.026597233833321]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 7,
					segment_name: 'Kürten Eichhof - Kürten Biesfeld',
					start_stop_name: 'Kürten Eichhof',
					end_stop_name: 'Kürten Biesfeld',
					segment_id: '3378 - 5075',
					start_stop_id: '3378',
					end_stop_id: '5075',
					distance_m: 1375.6961128069688
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.262615208089425, 51.026597233833321],
						[7.2591, 51.02503],
						[7.25739, 51.02391],
						[7.25641, 51.02286],
						[7.25425, 51.02203],
						[7.253, 51.02124],
						[7.25239, 51.02097],
						[7.25044, 51.02051],
						[7.24732, 51.02009],
						[7.246785062017566, 51.01992887410168]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 8,
					segment_name: 'Kürten Biesfeld - Kürten Miebach',
					start_stop_name: 'Kürten Biesfeld',
					end_stop_name: 'Kürten Miebach',
					segment_id: '5075 - 3380',
					start_stop_id: '5075',
					end_stop_id: '3380',
					distance_m: 1183.9670269323512
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.246785062017566, 51.01992887410168],
						[7.24566, 51.01959],
						[7.24436, 51.01953],
						[7.24394, 51.0194],
						[7.24365, 51.01921],
						[7.24283, 51.01807],
						[7.24215, 51.01748],
						[7.24082, 51.01682],
						[7.2385, 51.01603],
						[7.238, 51.01564],
						[7.23765, 51.01521],
						[7.23607, 51.01432],
						[7.23538, 51.01406],
						[7.2346, 51.0139],
						[7.233942621176471, 51.013831995294119]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 9,
					segment_name: 'Kürten Miebach - Kürten Steeg',
					start_stop_name: 'Kürten Miebach',
					end_stop_name: 'Kürten Steeg',
					segment_id: '3380 - 3381',
					start_stop_id: '3380',
					end_stop_id: '3381',
					distance_m: 858.41607830856867
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.233942621176471, 51.013831995294119],
						[7.2317, 51.0136],
						[7.22702, 51.01358],
						[7.22545, 51.01326],
						[7.22419, 51.01274],
						[7.22253716179918, 51.011896145897474]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 10,
					segment_name: 'Kürten Steeg - Kürten Dürscheid Kirche',
					start_stop_name: 'Kürten Steeg',
					end_stop_name: 'Kürten Dürscheid Kirche',
					segment_id: '3381 - 3382',
					start_stop_id: '3381',
					end_stop_id: '3382',
					distance_m: 519.72724152362366
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.22253716179918, 51.011896145897474],
						[7.22182, 51.01153],
						[7.22114, 51.01136],
						[7.22026, 51.01137],
						[7.2199, 51.01123],
						[7.21916, 51.0104],
						[7.21849, 51.00977],
						[7.21823, 51.00962],
						[7.216846088990826, 51.009578063302747]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 11,
					segment_name: 'Kürten Dürscheid Kirche - Kürten Spitze',
					start_stop_name: 'Kürten Dürscheid Kirche',
					end_stop_name: 'Kürten Spitze',
					segment_id: '3382 - 3354',
					start_stop_id: '3382',
					end_stop_id: '3354',
					distance_m: 1077.1783072691223
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.216846088990826, 51.009578063302747],
						[7.21658, 51.00957],
						[7.21459, 51.00932],
						[7.21435, 51.00923],
						[7.21421, 51.00905],
						[7.21425, 51.00884],
						[7.21511, 51.00838],
						[7.21507, 51.00811],
						[7.21484, 51.00801],
						[7.2145, 51.0079],
						[7.21374, 51.00784],
						[7.21186, 51.00796],
						[7.21159, 51.00788],
						[7.21124, 51.00759],
						[7.21092, 51.00745],
						[7.2106, 51.00748],
						[7.21023, 51.00773],
						[7.20864, 51.00942],
						[7.20822, 51.00964],
						[7.20774, 51.00977],
						[7.206805957425802, 51.009753394798686]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 12,
					segment_name: 'Kürten Spitze - Bergisch Gladbach Unterthal',
					start_stop_name: 'Kürten Spitze',
					end_stop_name: 'Bergisch Gladbach Unterthal',
					segment_id: '3354 - 3347',
					start_stop_id: '3354',
					end_stop_id: '3347',
					distance_m: 1068.7007849737433
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.206805957425802, 51.009753394798686],
						[7.20324, 51.00969],
						[7.2019, 51.00947],
						[7.20137, 51.00946],
						[7.19891, 51.00973],
						[7.19761, 51.00951],
						[7.19711, 51.00951],
						[7.1954, 51.00998],
						[7.19409, 51.01013],
						[7.19353, 51.01029],
						[7.19294, 51.01065],
						[7.192497821695762, 51.011050066084785]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 13,
					segment_name: 'Bergisch Gladbach Unterthal - Bergisch Gladbach Herrenstrunden',
					start_stop_name: 'Bergisch Gladbach Unterthal',
					end_stop_name: 'Bergisch Gladbach Herrenstrunden',
					segment_id: '3347 - 3346',
					start_stop_id: '3347',
					end_stop_id: '3346',
					distance_m: 1234.8341585069404
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.192497821695762, 51.011050066084785],
						[7.19231, 51.01122],
						[7.19188, 51.0115],
						[7.19152, 51.01164],
						[7.19079, 51.01181],
						[7.19028, 51.01185],
						[7.18936, 51.01176],
						[7.18732, 51.01115],
						[7.18643, 51.01078],
						[7.18314, 51.00843],
						[7.18165, 51.00787],
						[7.18135, 51.00762],
						[7.18121, 51.00724],
						[7.1809, 51.00693],
						[7.17931575129534, 51.005894145077718]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 14,
					segment_name: 'Bergisch Gladbach Herrenstrunden - Bergisch Gladbach Schiff',
					start_stop_name: 'Bergisch Gladbach Herrenstrunden',
					end_stop_name: 'Bergisch Gladbach Schiff',
					segment_id: '3346 - 3345',
					start_stop_id: '3346',
					end_stop_id: '3345',
					distance_m: 361.39698709804622
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.17931575129534, 51.005894145077718],
						[7.1783, 51.00523],
						[7.17597, 51.00453],
						[7.175176607722655, 51.004043485867669]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 15,
					segment_name: 'Bergisch Gladbach Schiff - Bergisch Gladbach Dombach',
					start_stop_name: 'Bergisch Gladbach Schiff',
					end_stop_name: 'Bergisch Gladbach Dombach',
					segment_id: '3345 - 3344',
					start_stop_id: '3345',
					end_stop_id: '3344',
					distance_m: 1847.9873649439483
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.175176607722655, 51.004043485867669],
						[7.17385, 51.00323],
						[7.17164, 51.00116],
						[7.17093, 50.99947],
						[7.17055, 50.99907],
						[7.16978, 50.99852],
						[7.16929, 50.99823],
						[7.16858, 50.99797],
						[7.16645, 50.99774],
						[7.16558, 50.99751],
						[7.16208, 50.99574],
						[7.16059, 50.99467],
						[7.15964, 50.9943],
						[7.1585, 50.9941],
						[7.15689, 50.99394],
						[7.156319031450987, 50.994012580747757]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 16,
					segment_name: 'Bergisch Gladbach Dombach - Bergisch Gladbach Heiligenstock',
					start_stop_name: 'Bergisch Gladbach Dombach',
					end_stop_name: 'Bergisch Gladbach Heiligenstock',
					segment_id: '3344 - 6688',
					start_stop_id: '3344',
					end_stop_id: '6688',
					distance_m: 687.72006066222752
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.156319031450987, 50.994012580747757],
						[7.15571, 50.99409],
						[7.15394, 50.99454],
						[7.15351, 50.99459],
						[7.15282, 50.99451],
						[7.14932, 50.99373],
						[7.14816, 50.99354],
						[7.14778, 50.9934],
						[7.147214467055446, 50.99306190965271]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 17,
					segment_name: 'Bergisch Gladbach Heiligenstock - Bergisch Gladbach Sonnenweg',
					start_stop_name: 'Bergisch Gladbach Heiligenstock',
					end_stop_name: 'Bergisch Gladbach Sonnenweg',
					segment_id: '6688 - 3343',
					start_stop_id: '6688',
					end_stop_id: '3343',
					distance_m: 175.76593708140797
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.147214467055446, 50.99306190965271],
						[7.14686, 50.99285],
						[7.144877999500832, 50.992618337603993]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 18,
					segment_name: 'Bergisch Gladbach Sonnenweg - Bergisch Gladbach Forum',
					start_stop_name: 'Bergisch Gladbach Sonnenweg',
					end_stop_name: 'Bergisch Gladbach Forum',
					segment_id: '3343 - 3305',
					start_stop_id: '3343',
					end_stop_id: '3305',
					distance_m: 847.69425230180047
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.144877999500832, 50.992618337603993],
						[7.14224, 50.99231],
						[7.14003, 50.99164],
						[7.13915, 50.99158],
						[7.1372, 50.9917],
						[7.13616, 50.99158],
						[7.13453, 50.99161],
						[7.133451870951037, 50.991037405146244]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 19,
					segment_name: 'Bergisch Gladbach Forum - Bergisch Gladbach Markt',
					start_stop_name: 'Bergisch Gladbach Forum',
					end_stop_name: 'Bergisch Gladbach Markt',
					segment_id: '3305 - 3314',
					start_stop_id: '3305',
					end_stop_id: '3314',
					distance_m: 396.76072372590636
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.133451870951037, 50.991037405146244],
						[7.13244, 50.9905],
						[7.13184, 50.99029],
						[7.131, 50.99019],
						[7.13056, 50.99017],
						[7.13025, 50.99056],
						[7.130024222558013, 50.991595462061525]
					]
				}
			},
			{
				type: 'Feature',
				properties: {
					shape_id: '1003',
					route_id: '1100426',
					route_name: '426',
					direction_id: 1,
					stop_sequence: 20,
					segment_name: 'Bergisch Gladbach Markt - Bergisch Gladbach (S)',
					start_stop_name: 'Bergisch Gladbach Markt',
					end_stop_name: 'Bergisch Gladbach (S)',
					segment_id: '3314 - 5208',
					start_stop_id: '3314',
					end_stop_id: '5208',
					distance_m: 495.55443770802941
				},
				geometry: {
					type: 'LineString',
					coordinates: [
						[7.130024222558013, 50.991595462061525],
						[7.12996, 50.99189],
						[7.12692, 50.99249],
						[7.12696, 50.99216],
						[7.12673, 50.99195],
						[7.124775747297698, 50.990992222685506]
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

				result.forEach((segment) => {
					let startStopLabel = segment['properties']['start_stop_name'];
					let startStopLngLat = segment['geometry']['coordinates'][0];
					let popup = new Popup({ offset: 25 }).setText(startStopLabel);
					new Marker().setLngLat(startStopLngLat).setPopup(popup).addTo(map);
				});
			});
		});
		console.log(results);

		results.forEach((result) => {
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
