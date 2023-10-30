<script>
	import Map from '../components/Map/Map.svelte';

	import SearchPopOver from '../components/Popover/SearchPopOver.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import BStopPopover from '../components/Popover/BStopPopover.svelte';
	import CongestionButton from '../components/CongestionButton.svelte';
</script>

<body>
	<Map>
		<BStopPopover />
		<SearchPopOver />
		<BLinePopover />
		<CongestionButton />
	</Map>
</body>
