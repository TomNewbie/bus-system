<script>
	// @ts-nocheck
	import BusLineItem from '../BusLineItem.svelte';
	import { busNetwork, currentIndex } from '../../stores/stores';

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

	let searchTerm = '';
</script>

<body>
	<div class={containerClass} class:hidden={!listPopOver}>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex px-4 py-8 popover-search bg-white/50 rounded-t-xl"
			>
				<input
					type="text"
					class="w-5/6 border border-gray-300 rounded-xl px-8 py-2 focus:border-black"
					bind:value={searchTerm}
					placeholder="Search..."
					on:click={() => toggleTransform('input')}
				/>

				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<img
					src="./times.svg"
					alt="times-icon"
					class="absolute ml-2 w-8 h-8 rounded-full exit-button bg-slate-200/60 right-2"
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
				{#each $busNetwork as busLine, index}
					{#if busLine[0].properties.route_id.includes(searchTerm) || searchTerm == '' || busLine[0].properties.start_stop_name
							.toLowerCase()
							.includes(searchTerm.toLowerCase()) || busLine[busLine.length - 1].properties.end_stop_name
							.toLowerCase()
							.includes(searchTerm.toLowerCase())}
						<BusLineItem
							bus_id={busLine[0].properties.route_id}
							bus_start={busLine[0].properties.start_stop_name}
							bus_end={busLine[busLine.length - 1].properties.end_stop_name}
							handleClick={() => {
								currentIndex.set(index);
								listPopOver = false;
							}}
						/>
					{/if}
				{/each}
			</div>
		</div>
	</div>
</body>
