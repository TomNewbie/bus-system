<script>
	// @ts-nocheck

	import BusLineItem from '../BusLineItem.svelte';
	import {
		searchPopoverVisible,
		busLinePopoverVisible,
		busStopPopoverVisible
	} from '../../stores/stores';
	import { onMount } from 'svelte';

	let isTransformed = false;

	// @ts-ignore
	function toggleTransform(source) {
		if (source === 'cancel') {
			isTransformed = false; // Clicking "Cancel" sets isTransformed to false
		} else if (source === 'input') {
			isTransformed = true; // Clicking the input sets isTransformed to true
		}
	}

	$: containerClass = `absolute bottom-0 z-10 w-1/4 transition-transform duration-500 transform right-10 bg-white/90 rounded-t-xl  ${
		isTransformed ? 'h-9/10' : 'h-1/8'
	}`;

	$: inputClass = `w-3/4 py-1 border border-solid rounded-xl border-neutral-30 ${
		isTransformed ? 'w-3/4' : 'w-full'
	}`;

	let endpoint = 'http://localhost:8000/bus-lines';
	// @ts-ignore
	let busLines = [];

	onMount(async function () {
		const response = await fetch(endpoint);
		const data = await response.json();
		console.log(data);
		busLines = data;
	});

	function navigateToBusLine() {
		toggleTransform('cancel');
		searchPopoverVisible.update((value) => !value);
		busLinePopoverVisible.update((value) => !value);
	}

	// @ts-ignore
	function navigateToBusStop() {
		toggleTransform('cancel');
		searchPopoverVisible.update((value) => !value);
		busStopPopoverVisible.update((value) => !value);
	}
</script>

<body>
	<div class={containerClass} class:hidden={!$searchPopoverVisible}>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex items-center justify-around px-4 py-4 popover-search bg-white/50 rounded-t-xl"
			>
				<input
					on:click={() => toggleTransform('input')}
					placeholder="Search for bus line or bus stop"
					class={inputClass}
				/>
				<button
					class:hidden={!isTransformed}
					on:click={() => toggleTransform('cancel')}
					class="text-base">Cancel</button
				>
			</div>
			<div
				class="flex flex-col flex-grow gap-4 overflow-y-auto popover-scroll last:border-b-2 last:border-t-0 last:pb-4"
				style="height: calc(100vh - 130px); "
			>
				{#each busLines as busLine}
					<BusLineItem
						bus_id={busLine.route_id}
						bus_start={busLine.start_stop_name}
						bus_end={busLine.end_stop_name}
						handleClick={() => navigateToBusLine()}
					/>
				{/each}
			</div>
		</div>
	</div>
</body>

<style>
	/* Add margin to the input's placeholder */
	input::placeholder {
		margin-left: 10px;
		@apply text-base;
	}

	/* Add padding to the input to create spacing when text is entered */
	input {
		padding-left: 10px;
		@apply text-base;
	}
</style>
