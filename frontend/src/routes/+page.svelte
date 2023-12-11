<script>
	import { Router, Route } from 'svelte-routing';
	import Home from '../components/Home.svelte';
	import MapCa from '../components/MapCA.svelte';
	import MapDe from '../components/MapDE.svelte';

	export let baseUrl = 'http://127.0.0.1:5173/';
	export let path = '';

	let url = baseUrl + path; // Updated URL construction

	// Make sure to handle changes in the path variable
	$: url = baseUrl + path;
</script>

<Router {url}>
	<div>
		<Route path="/de" component={MapDe} />
		<Route path="/ca" component={MapCa} />
		<Route path="" component={Home} />
	</div>
</Router>
