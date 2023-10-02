<script>
	import BusLineItem from '../components/BusLineItem.svelte';
	import Map from '../components/Map/Map.svelte';
	import MapMarker from '../components/Map/MapMarker.svelte';
	import SearchPopOver from '../components/Popover/SearchPopOver.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import BStopPopover from '../components/Popover/BStopPopover.svelte';
</script>

<body>
	<Map>
		<!-- <BStopPopover stop_id={12} stop_name={'The Trillium'} /> -->
		<SearchPopOver />
		<!-- <BLinePopover bus_id={1} stop_start={'Blk 307A'} stop_end={'Bishan Stn'} number_stops={7} /> -->
	</Map>
</body>
