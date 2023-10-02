<script>
	// @ts-nocheck

	import BusLineTag from '../BusLineTag.svelte';
	// @ts-ignore
	export let stop_id;
	// @ts-ignore
	export let stop_name;
	export let number_bus_line = 1;

	let isTransformed = false;

	// @ts-ignore
	function toggleTransform() {
		!isTransformed;
	}

	$: containerClass = `absolute bottom-0 z-10 w-1/4 pb-0 mb-0 transition-transform duration-500 transform right-10 bg-white/90 rounded-t-xl   ${
		isTransformed ? 'hidden' : 'h-1/2'
	}`;
</script>

<body>
	<div class={containerClass}>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex items-start justify-start p-4 py-4 popover-stop bg-white/50 rounded-t-xl"
				style="height: 9vh;"
			>
				<div class="flex items-center h-full gap-x-1">
					<div
						class=" bg-[#F7DFDE] text-[#F01B48] px-4 py-1 font-semibold rounded-md border-solid border-2 border-white text-base mr-2"
					>
						{stop_id}
					</div>

					<div class="text-xl font-bold text-black">{stop_name}</div>
					<img
						src="./times.svg"
						alt="times-icon"
						class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-4"
					/>
				</div>
			</div>
			<div class="p-4 pb-0">
				<p class="text-base text-slate-800">{number_bus_line} SERVICES</p>
			</div>
			<div
				class="flex flex-wrap p-4 gap-x-14 gap-y-2 popover-scroll"
				style="max-height: calc(100vh - 59vh); overflow-y: auto;"
			>
				{#each [1, 2, 3, 4, 5, 6, 7, 1011, 11, 9] as item}
					<BusLineTag bus_id={item} />
				{/each}
			</div>
		</div>
	</div>
</body>
