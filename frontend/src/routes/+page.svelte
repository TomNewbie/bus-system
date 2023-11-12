<script>
	import Map from '../components/Map/Map.svelte';
	import SearchPopOver from '../components/Popover/ListPopOver.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import CongestionButton from '../components/CongestionButton.svelte';
</script>

<body>
	<Map>
		<SearchPopOver />
		<BLinePopover />
		<CongestionButton />
	</Map>
</body>
