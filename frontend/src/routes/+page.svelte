<script>
	import Map from '../components/Map/Map.svelte';

	import SearchPopOver from '../components/Popover/SearchPopOver.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
</script>

<body>
	<Map>
		<SearchPopOver />
		<BLinePopover />
	</Map>
</body>
