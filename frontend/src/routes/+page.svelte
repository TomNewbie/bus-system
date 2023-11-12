<script>
	import Map from '../components/Map/Map.svelte';
	import ListPopover from '../components/Popover/ListPopover.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import CongestionButton from '../components/CongestionButton.svelte';
</script>

<body>
	<Map>
		<ListPopover />
		<BLinePopover />
		<CongestionButton />
	</Map>
</body>
