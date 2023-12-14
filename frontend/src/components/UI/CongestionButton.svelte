<script>
	// @ts-nocheck
	import { canReroute, currentIndex, minute } from '../../stores/stores';

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
		minute.set(0);
		busLinePopoverVisible = false;
		time = '';
		isOpen = false;
	}

	let isOpen = false;
	let items = ['Choose time to predict', 'Next 10 minutes', 'Next 20 minutes', 'Next 30 minutes'];
	let times = [0, 10, 20, 30];
	let time = '';
	let valueToFetch = 0;
	function updateTime(index) {
		time = items[index];
		minute.set(times[index]);
		canReroute.set(false);
		isOpen = false;
	}

	const congestionColors = [
		'#B7EB8F', // Congestion level 1
		'#FFE58F', // Congestion level 2
		'#FFA500', // Congestion level 3
		'#FF0000', // Congestion level 4
		'#B60606' // Congestion level 5
	];
</script>

<body class="relative flex justify-end mt-3 mr-3" class:hidden={!busLinePopoverVisible}>
	<div class="absolute flex justify-center p-4 bg-white rounded-lg">
		<!-- Dropdown -->
		<div class="mr-4">
			<button
				on:click={() => (isOpen = !isOpen)}
				class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border rounded-lg shadow-sm cursor-pointer dropdown"
			>
				{#if !time}Choose time to predict{/if} <span class="ml-1">{time}</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="inline-block w-4 h-4 ml-2"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M19 9l-7 7-7-7"
					/>
				</svg>
			</button>

			{#if isOpen}
				<div class="absolute items-center mt-2 bg-white border rounded-lg">
					{#each items as item, index}
						<!-- svelte-ignore a11y-click-events-have-key-events -->
						<!-- svelte-ignore a11y-no-static-element-interactions -->
						<div
							class="block px-4 py-2 text-sm text-gray-800 transition-colors hover:bg-gray-100 dropdown-item"
							style="cursor: pointer;"
							on:click={() => {
								updateTime(index);
							}}
						>
							{item}
						</div>
					{/each}
				</div>
			{/if}
		</div>
		<!-- Dropdown -->

		<!-- Congestion level -->
		<div class="flex flex-col justify-center">
			<div class="flex justify-between">
				<p>Fast(0)</p>
				<p>Slow(4)</p>
			</div>
			<div class="flex">
				<div class="w-8 h-4 bg-[#43D224] border-gray-600 focus:outline-none" />
				<div class="w-8 h-4 bg-[#FFE58F] border-gray-600 focus:outline-none" />
				<div class="w-8 h-4 bg-[#FFA500] border-gray-600 focus:outline-none" />
				<div class="w-8 h-4 bg-[#FC7A7A] border-gray-600 focus:outline-none" />
				<div class="w-8 h-4 bg-[#B60606] border-gray-600 focus:outline-none" />
			</div>
		</div>
	</div>
</body>
