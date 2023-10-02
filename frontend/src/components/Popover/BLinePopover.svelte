<script>
	// @ts-nocheck

	import BusStopTag from '../BusStopTag.svelte';
	import { searchPopoverVisible, busLinePopoverVisible } from '../../stores/stores';

	// @ts-ignore
	export let bus_id;
	export let stop_start;
	export let stop_end;
	export let number_stops;

	// @ts-ignore
	function navigateToSearch() {
		searchPopoverVisible.update((value) => !value);
		busLinePopoverVisible.update((value) => !value);
	}

	let busStops = [
		{ stop_id: 1, stop_name: 'Blk 1', is_last_stop: false },
		{ stop_id: 2, stop_name: 'Blk 2', is_last_stop: false },
		{ stop_id: 3, stop_name: 'Blk 3', is_last_stop: false },
		{ stop_id: 4, stop_name: 'Blk 4', is_last_stop: false },
		{ stop_id: 5, stop_name: 'Blk 5', is_last_stop: false },
		{ stop_id: 6, stop_name: 'Blk 6', is_last_stop: false },
		{ stop_id: 7, stop_name: 'Blk 7', is_last_stop: true }
	];
</script>

<body>
	<div
		class:hidden={!$busLinePopoverVisible}
		class="absolute bottom-0 z-10 w-1/4 pb-0 mb-0 transition-transform duration-500 transform right-10 bg-white/90 rounded-t-xl h-9/10"
	>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex items-start justify-start p-4 py-4 popover-stop bg-white/50 rounded-t-xl"
				style="height: 9vh;"
			>
				<div class="flex items-center h-full gap-x-1">
					<div
						class="mr-2 bg-[#DBF6D0] text-[#3A6727] px-3 py-1 font-semibold rounded-md border-solid border-2 border-white text-base"
					>
						{bus_id}
					</div>

					<div class="text-xl font-bold text-black">{stop_start} → {stop_end}</div>
					<!-- svelte-ignore a11y-click-events-have-key-events -->
					<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
					<img
						src="./times.svg"
						alt="times-icon"
						class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-4"
						on:click={() => navigateToSearch()}
						style="cursor: pointer;"
					/>
				</div>
			</div>
			<div class="p-4 pb-0">
				<p class="text-base text-slate-800">{number_stops} STOPS</p>
			</div>
			<div
				class="p-4 gap-x-14 gap-y-2 popover-scroll"
				style="height: calc(100vh - 130px); overflow-y: auto;"
			>
				{#each busStops as busStop}
					<BusStopTag
						stop_id={busStop.stop_id}
						stop_name={busStop.stop_name}
						is_last_stop={busStop.is_last_stop}
					/>
				{/each}
			</div>
		</div>
	</div>
</body>
