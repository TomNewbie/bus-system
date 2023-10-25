<script>
	// @ts-nocheck

	import BusStopTag from '../BusStopTag.svelte';
	import {
		searchPopoverVisible,
		busLinePopoverVisible,
		busStopPopoverVisible,
		currentBusLine,
		currentBusStop,
		currentIndex
	} from '../../stores/stores';

	// @ts-ignore
	function navigateToSearch() {
		searchPopoverVisible.update((value) => true);
		busLinePopoverVisible.update((value) => false);
		currentIndex.update((value) => -1);
		console.log($searchPopoverVisible);
		console.log($busLinePopoverVisible);
	}

	// @ts-ignore
	function navigateToBusStop(stop) {
		busLinePopoverVisible.update((value) => !value);
		busStopPopoverVisible.update((value) => !value);
		currentBusStop.update((value) => stop);
	}

	let endpoint = ''; // Initialize the endpoint

	let isLoading = true; // Add a loading flag
	let busLine;

	$: {
		busLine = $currentBusLine; // Update busLine when currentBusLine changes
		fetchBusLineData();
	}

	// @ts-ignore
	let busStops = [];
	let route_id;
	let start_stop_name;
	let end_stop_name;
	let number_stops;
	// Function to fetch bus line data
	function fetchBusLineData() {
		if (busLine == 0) return;
		busStops = [];
		isLoading = true;
		route_id = busLine[0].properties.route_id;
		start_stop_name = busLine[0].properties.start_stop_name;
		end_stop_name = busLine[busLine.length - 1].properties.end_stop_name;

		busLine.forEach((busStop, index) => {
			busStops.push({
				stop_id: busStop.properties.start_stop_id,
				stop_name: busStop.properties.start_stop_name,
				is_last_stop: false
			});
			if (index == busLine.length - 1) {
				busStops.push({
					stop_id: busStop.properties.end_stop_id,
					stop_name: busStop.properties.end_stop_name,
					is_last_stop: true
				});
			}
		});
		if (busStops) number_stops = busStops.length;
		else number_stops = 0;

		isLoading = false; // Set loading flag to false when data is loaded
	}
</script>

<body>
	<div
		class:hidden={!$busLinePopoverVisible}
		class="absolute bottom-0 z-10 w-1/4 mb-0 transition-transform duration-500 transform left-10 bg-white/90 rounded-t-xl h-9/10"
	>
		{#if isLoading}
			<!-- Check if data is loading -->
			<p>Loading...</p>
			<!-- Display loading message -->
		{:else}
			<div>
				<div
					class="sticky top-0 left-0 right-0 flex flex-wrap items-start p-4 py-4 shadow-md popover-stop bg-white/50 rounded-t-xl"
					style="height:fit-content"
				>
					<div class="flex items-center h-full gap-x-1">
						<div
							class="mr-2 bg-[#DBF6D0] text-[#3A6727] px-2 py-1 font-semibold rounded-md border-solid border-2 border-white text-base"
						>
							{route_id}
						</div>

						<div class="h-full mr-6 text-base font-bold text-black">
							{start_stop_name} →{end_stop_name}
						</div>
						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
						<img
							src="./times.svg"
							alt="times-icon"
							class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-2"
							on:click={() => navigateToSearch()}
							style="cursor: pointer;"
						/>
					</div>
					<div class="p-4 pb-0">
						<p class="text-base text-slate-800">
							{number_stops} STOPS
						</p>
					</div>
				</div>

				<div
					class="pt-4 pb-8 m-2 mt-0 mr-0 popover-scroll"
					style="height: calc(90vh - 120px); overflow-y: auto;"
				>
					{#if busStops && busStops.length > 0}
						{#each busStops as busStop}
							<BusStopTag
								stop_id={busStop.stop_id}
								stop_name={busStop.stop_name}
								is_last_stop={busStop.is_last_stop}
							/>
						{/each}
					{/if}
				</div>
			</div>
		{/if}
	</div>
</body>
