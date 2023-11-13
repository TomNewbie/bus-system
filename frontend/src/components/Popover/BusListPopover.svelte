<script>
	// @ts-nocheck
	import BusLineItem from '../BusLineItem.svelte';
	import { allBusLines, currentIndex } from '../../stores/stores';

	let isTransformed = true;
	let listPopOver = true;
	// @ts-ignore
	function toggleTransform(source) {
		if (source === 'cancel') {
			isTransformed = false;
		} else if (source === 'input') {
			isTransformed = true;
		}
	}

	$: containerClass = `absolute bottom-0 z-10 w-1/4 transition-transform duration-500 transform left-10 bg-white/90 rounded-t-xl  ${
		isTransformed ? 'h-9/10' : 'h-1/10'
	}`;

	$: inputClass = `w-3/4 py-1 border border-solid rounded-xl border-neutral-30 ${
		isTransformed ? 'w-3/4' : 'w-full'
	}`;

	// @ts-ignore
	$: {
		triggerSearchBar($currentIndex);
		onCurrentBusline($currentIndex);
	}

	function onCurrentBusline(index) {
		if (index === -1) return;
		listPopOver = false;
	}

	function triggerSearchBar(index) {
		if (index !== -1) return;
		listPopOver = true;
		isTransformed = true;
	}

	let searchId = '';
	let isSearched = false;
	$: {
		searchId;
	}
	let isLoading = false; // Add a loading flag
	let isError = false;
	let searchBus = {};

	function fetchSearchBusLine() {
		console.log(searchId);
		const endpoint = 'http://localhost:8000/bus-lines/' + searchId;
		isLoading = true;
		isError = false; // Reset the error flag

		fetch(endpoint)
			.then((response) => {
				if (response.status === 200) {
					return response.json();
				} else if (response.status === 404) {
					isError = true; // Set error flag
					return Promise.reject('Resource not found');
				} else {
					isError = true; // Set error flag
					return Promise.reject(`API request failed with status code ${response.status}`);
				}
			})
			.then((data) => {
				searchBus = data;
				console.log(searchBus);
			})
			.catch((error) => {
				console.log(error);
			})
			.finally(() => {
				isLoading = false; // Set isLoading to false after the request completes
			});
	}

	// Custom event handler to update searchId
	function updateSearchId(event) {
		searchId = event.target.value;
		if (searchId == '') {
			isSearched = false;
			isLoading = false;
			isError = false;
		} else {
			isSearched = true;
			fetchSearchBusLine(searchId);
		}
	}
</script>

<body>
	<div class={containerClass} class:hidden={!listPopOver}>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex items-center justify-around px-4 py-4 popover-search bg-white/50 rounded-t-xl"
			>
				<button on:click={() => toggleTransform('input')} class="text-base text-black font-regular"
					>List of bus lines</button
				>
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<img
					src="./times.svg"
					alt="times-icon"
					class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-2"
					class:hidden={!isTransformed}
					on:click={() => toggleTransform('cancel')}
					style="cursor: pointer;"
				/>
			</div>
			<div
				class="flex flex-col flex-grow gap-4 overflow-y-auto popover-scroll last:border-b-2 last:border-t-0 last:pb-4"
				class:hidden={!isTransformed}
				style="height: calc(100vh - 130px); "
			>
				{#if isLoading}
					<div>Loading</div>
				{:else if isSearched && !isLoading && isError}
					<div>Not Found</div>
				{:else if isSearched}
					<BusLineItem
						bus_id={searchBus.route_id}
						bus_start={searchBus.start_stop_name}
						bus_end={searchBus.end_stop_name}
						handleClick={() => {
							currentIndex.set(Number(searchBus.route_id));
							listPopOver = false;
						}}
					/>
				{:else}
					{#each $allBusLines as busLine, index}
						<BusLineItem
							bus_id={busLine[0].properties.route_id}
							bus_start={busLine[0].properties.start_stop_name}
							bus_end={busLine[busLine.length - 1].properties.end_stop_name}
							handleClick={() => {
								currentIndex.set(index);
								listPopOver = false;
							}}
						/>
					{/each}
				{/if}
			</div>
		</div>
	</div>
</body>
