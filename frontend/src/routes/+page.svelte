<script>
	import Map from '../components/Map/Map.svelte';
	import BusListPopover from '../components/Popover/BusListPopover.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import CongestionButton from '../components/CongestionButton.svelte';
	import ChooseModelButton from '../components/ChooseModelButton.svelte';
	import Toast from '../components/Toast.svelte';
</script>

<body>
	<Map>
		<BusListPopover />
		<BLinePopover />
		<CongestionButton />
		<ChooseModelButton />
		<Toast />
	</Map>
</body>
