<script>
	import Map from '../components/Map/Map.svelte';
	import BusListPopover from '../components/Popover/BusListPopover.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import CongestionButton from '../components/UI/CongestionButton.svelte';
	import ChooseModelButton from '../components/UI/ChooseModelButton.svelte';
	import Toast from '../components/UI/Toast.svelte';
</script>

<Map api="http://localhost:8000/ca/segments">
	<BusListPopover />
	<BLinePopover />
	<CongestionButton />
	<ChooseModelButton />
	<Toast />
</Map>
