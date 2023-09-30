<script>
	import BusLineItem from './BusLineItem.svelte';
	// @ts-ignore
	import BusStopItem from './BusStopItem.svelte';

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
</script>

<body>
	<div class={containerClass}>
		<div class="relative">
			<div
				class="sticky top-0 left-0 right-0 flex items-center justify-around px-4 py-4 popover-search bg-white/50 rounded-t-xl"
			>
				<input
					on:click={() => toggleTransform('input')}
					placeholder="Search for bus line or bus stop"
					class="w-3/4 py-1 border border-solid rounded-xl border-neutral-30"
				/>
				<button on:click={() => toggleTransform('cancel')} class="text-base">Cancel</button>
			</div>
			<div
				class="flex flex-col flex-grow gap-4 overflow-y-auto popover-scroll last:border-b-2 last:border-t-0 last:pb-4"
				style="height: calc(100vh - 130px);"
			>
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
				<BusLineItem bus_id={12} bus_start={'Blk 151'} bus_end={'Lakeside Stn'} />
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
