<script>
	import Map from '../components/Map/Map.svelte';
	import BusListPopover from '../components/Popover/BusListPopover.svelte';
	import BLinePopover from '../components/Popover/BLinePopover.svelte';
	import CongestionButton from '../components/UI/CongestionButton.svelte';
	import ChooseModelButton from '../components/UI/ChooseModelButton.svelte';
	import Toast from '../components/UI/Toast.svelte';
	import ReroutingButton from './UI/ReroutingButton.svelte';
</script>

<Map api="http://188.166.180.176:8000/ca/segments">
	<BusListPopover />
	<BLinePopover />
	<CongestionButton />
	<ChooseModelButton />
	<Toast />
	<ReroutingButton />
</Map>
