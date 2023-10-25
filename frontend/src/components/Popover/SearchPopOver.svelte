<script>
	// @ts-nocheck
	import BusLineItem from '../BusLineItem.svelte';
	import {
		searchPopoverVisible,
		busLinePopoverVisible,
		busStopPopoverVisible,
		currentBusLine,
		hehe,
		currentIndex
	} from '../../stores/stores';
	import { onMount } from 'svelte';

	// Create an event dispatcher

	let isTransformed = $searchPopoverVisible;

	// @ts-ignore
	function toggleTransform(source) {
		if (source === 'cancel') {
			isTransformed = false; // Clicking "Cancel" sets isTransformed to false
		} else if (source === 'input') {
			isTransformed = true; // Clicking the input sets isTransformed to true
		}
	}

	$: containerClass = `absolute bottom-0 z-10 w-1/4 transition-transform duration-500 transform left-10 bg-white/90 rounded-t-xl  ${
		isTransformed ? 'h-9/10' : 'h-1/10'
	}`;

	$: inputClass = `w-3/4 py-1 border border-solid rounded-xl border-neutral-30 ${
		isTransformed ? 'w-3/4' : 'w-full'
	}`;

	// @ts-ignore
	$: busLines = $hehe;
	// $: triggerSearchBar($currentIndex);
	function triggerSearchBar() {
		isTransformed = true;
	}
	onMount(async function () {
		console.log($hehe);
	});

	function navigateToBusLine(busLine) {
		toggleTransform('cancel');
		searchPopoverVisible.update((value) => false);
		busLinePopoverVisible.update((value) => true);
		currentBusLine.update((value) => busLine);
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
				class:hidden={!isTransformed}
				style="height: calc(100vh - 130px); "
			>
				{#each busLines as busLine, index}
					<BusLineItem
						bus_id={busLine[0].properties.route_id}
						bus_start={busLine[0].properties.start_stop_name}
						bus_end={busLine[busLine.length - 1].properties.end_stop_name}
						handleClick={() => {
							console.log('hhehee');
							currentIndex.set(index);
							searchPopoverVisible.update((value) => false);
							busLinePopoverVisible.update((value) => true);
							currentBusLine.update((value) => busLine);
						}}
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
