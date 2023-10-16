<script>
	import BusLineItem from '../components/BusLineItem.svelte';
	import Map from '../components/Map/Map.svelte';
	import MapMarker from '../components/Map/MapMarker.svelte';
	import SearchPopOver from '../components/Popover/SearchPopOver.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import BStopPopover from '../components/Popover/BStopPopover.svelte';
	import Button from '../components/Button.svelte';
</script>

<body>
	<Map>
		<BStopPopover />
		<SearchPopOver />
		<BLinePopover />
	</Map>
</body>
