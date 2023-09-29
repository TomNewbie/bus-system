<script>
	import BusLineItem from '../BusLineItem.svelte';
	import Map from '../Map.svelte';
	import MapMarker from '../MapMarker.svelte';
	import SearchPopOver from '../SearchPopOver.svelte';
	import BLinePopover from '../BLinePopover.svelte';
</script>

<body>
	<Map lat={35} lon={-84} zoom={3.5}>
		<BLinePopover />
	</Map>
</body>
