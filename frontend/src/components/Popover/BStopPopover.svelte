<script>
	// @ts-nocheck

	import BusLineTag from '../BusLineTag.svelte';
	import {
		busLinePopoverVisible,
		busStopPopoverVisible,
		currentBusStop
	} from '../../stores/stores';

	function navigateToBusLine() {
		busLinePopoverVisible.update((value) => !value);
		busStopPopoverVisible.update((value) => !value);
	}

	let endpoint = ''; // Initialize the endpoint
	let busStop = ''; // Initialize the busStop
	let isLoading = true; // Add a loading flag

	$: {
		busStop = $currentBusStop; // Update busLine when currentBusLine changes
		endpoint = `http://localhost:8000/bus-stops/${busStop}`;

		// Fetch data whenever the endpoint changes
		fetchBusLineData();
	}
	let stop_id;
	let stop_name;
	let number_routes;
	let routes = [];

	// Function to fetch bus line data
	async function fetchBusLineData() {
		if (endpoint) {
			isLoading = true; // Set loading flag to true
			const response = await fetch(endpoint);
			const data = await response.json();

			stop_id = data.stop_id;
			stop_name = data.stop_name;
			routes = data.routes;
			if (routes) number_routes = routes.length;
			else number_routes = 0;
			isLoading = false; // Set loading flag to false when data is loaded
		}
	}
</script>

<body>
	<div
		class:hidden={!$busStopPopoverVisible}
		class="absolute bottom-0 z-10 w-1/4 pb-0 mb-0 transition-transform duration-500 transform left-10 bg-white/90 rounded-t-xl h-9/10"
	>
		{#if isLoading}
			<!-- Check if data is loading -->
			<p>Loading...</p>
			<!-- Display loading message -->
		{:else}
			<div class="relative">
				<div
					class="sticky top-0 left-0 right-0 flex items-start justify-start p-4 py-4 shadow-md popover-stop bg-white/50 rounded-t-xl"
				>
					<div class="flex items-center h-full gap-x-1">
						<div
							class=" bg-[#F7DFDE] text-[#F01B48] px-2 py-1 font-semibold rounded-md border-solid border-2 border-white text-base mr-2"
						>
							{stop_id}
						</div>

						<div class="text-base font-bold text-black">{stop_name}</div>

						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
						<img
							src="./times.svg"
							alt="times-icon"
							class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-2"
							on:click={() => navigateToBusLine()}
							style="cursor: pointer;"
						/>
					</div>
				</div>
				<div class="p-4 pb-0">
					<p class="text-base text-slate-800">{number_routes} SERVICES</p>
				</div>
				<div
					class="flex flex-wrap p-4 gap-x-14 gap-y-2 popover-scroll"
					style="max-height: calc(100vh - 59vh); overflow-y: auto;"
				>
					{#each routes as route}
						<BusLineTag bus_id={route.route_id} />
					{/each}
				</div>
			</div>
		{/if}
	</div>
</body>
