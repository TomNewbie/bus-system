<script>
	// @ts-nocheck

	import BusStopTag from '../BusStopTag.svelte';

	// @ts-ignore
	export let bus_id;
	// @ts-ignore
	export let stop_start;
	export let stop_end;
	export let number_stops;
</script>

<body>
	<div
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
					<img
						src="./times.svg"
						alt="times-icon"
						class="absolute w-8 h-8 rounded-full bg-slate-200/60 right-4"
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
				<BusStopTag stop_id={12} stop_name={'Blk 307A'} />
				<BusStopTag stop_id={13} stop_name={'Blk 307B'} />
				<BusStopTag stop_id={19996} stop_name={'Blk 307C'} />
				<BusStopTag stop_id={23} stop_name={'Blk 307D'} />
				<BusStopTag stop_id={36} stop_name={'Blk 307E'} />
				<BusStopTag stop_id={36} stop_name={'Blk 307F'} />
				<BusStopTag stop_id={123} stop_name={'Bishan Stn'} is_last_stop={true} />
			</div>
		</div>
	</div>
</body>
