<script>
	import { isToastShowed } from '../../stores/stores';
	import { fly } from 'svelte/transition';
	function closeToast() {
		$isToastShowed = false;
	}

	// Watch for changes in isToastShowed and show/hide the toast accordingly
	$: {
		if ($isToastShowed) {
			setTimeout(() => {
				$isToastShowed = false;
			}, 2000); // Delay of 0.5 seconds before hiding the toast
		}
	}
</script>

{#if $isToastShowed}
	<div
		transition:fly={{ x: '100%' }}
		class="absolute right-0 flex items-center justify-center mb-8 mr-2 top-36"
	>
		<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
		<div
			id="toast-default"
			class="flex items-center w-full max-w-xs p-4 text-white rounded-lg shadow bg-[#43D224]/90"
			role="alert"
		>
			<div class="mr-8 text-sm font-normal">Data fetched successfully!</div>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<img
				src="./times.svg"
				alt="times-icon"
				class="absolute w-8 h-8 rounded-full exit-button-busline bg-slate-200/60 right-2"
				on:click={() => closeToast()}
				style="cursor: pointer;"
			/>
		</div>
	</div>
{/if}
