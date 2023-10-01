<script>
	import BusLineItem from '../BusLineItem.svelte';
	import Map from '../Map.svelte';
	import MapMarker from '../MapMarker.svelte';
	import SearchPopOver from '../SearchPopOver.svelte';
	import BLinePopover from '../BLinePopover.svelte';
	import BStopPopover from '../BStopPopover.svelte';
</script>

<body>
	<Map>
		<!-- <BStopPopover stop_id={12} stop_name={'The Trillium'} /> -->
		<!-- <SearchPopOver /> -->
		<BLinePopover bus_id={1} stop_start={'Blk 307A'} stop_end={'Bishan Stn'} number_stops={7} />
	</Map>
</body>
