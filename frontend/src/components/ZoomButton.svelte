<script>
	export let label; // Make the label prop exportable
</script>

<button id="zoomto" class="btn-control">Zoom in line</button>

<style>
	.btn-control {
		font: bold 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
		background-color: #3386c0;
		color: #fff;
		position: absolute;
		top: 20px;
		left: 50%;
		z-index: 1;
		border: none;
		width: 200px;
		margin-left: -100px;
		display: block;
		cursor: pointer;
		padding: 10px 20px;
		border-radius: 3px;
	}

	.btn-control:hover {
		background-color: #4ea0da;
	}
</style>
