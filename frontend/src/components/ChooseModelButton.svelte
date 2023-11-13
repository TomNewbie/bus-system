<script>
	// @ts-nocheck
	import { currentIndex, minute } from '../stores/stores';

	let busLinePopoverVisible;
	$: {
		setupButtonState($currentIndex);
	}

	function setupButtonState(currentIndex) {
		if (currentIndex != -1) {
			busLinePopoverVisible = true;
		} else {
			setDefaultState();
		}
	}

	function setDefaultState() {
		busLinePopoverVisible = false;
	}
</script>

<body class="relative flex justify-end mt-20 mr-3" class:hidden={!busLinePopoverVisible}>
	<div class="absolute flex justify-center gap-4">
		<button class="px-3 py-2 bg-white rounded-lg active:bg-[#43D224] hover:bg-[#43D224]"
			>LSTM</button
		>
		<button class="px-3 py-2 bg-white rounded-lg active:bg-[rgb(67,210,36)] hover:bg-[#43D224]">
			Random Forest
		</button>
	</div>
</body>
