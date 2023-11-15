<script>
	// @ts-nocheck
	import { currentIndex, minute, model } from '../stores/stores';
	import { lstmModel, randomForestModel } from '../utils/constants';

	let busLinePopoverVisible;
	$: {
		setupButtonState($currentIndex);
	}

	function toggleButton(buttonId) {
		model.set(buttonId);
	}

	function setupButtonState(currentIndex) {
		if (currentIndex != -1) {
			busLinePopoverVisible = true;
		} else {
			busLinePopoverVisible = false;
		}
	}
</script>

<body class="relative flex justify-end mt-20 mr-3" class:hidden={!busLinePopoverVisible}>
	<div class="absolute flex justify-center gap-4">
		<button
			on:click={() => toggleButton(lstmModel)}
			class:activeButton={$model === lstmModel}
			class="px-3 py-2 bg-white rounded-lg active:bg-[#43D224] hover:bg-[#43D224] focus:outline-none]"
			>LSTM</button
		>
		<button
			on:click={() => toggleButton(randomForestModel)}
			class:activeButton={$model === randomForestModel}
			class="px-3 py-2 bg-white rounded-lg active:bg-[#43D224] hover:bg-[#43D224] focus:outline-none"
		>
			Random Forest
		</button>
	</div>
</body>

<style>
	.activeButton {
		background-color: #43d224;
	}
</style>
