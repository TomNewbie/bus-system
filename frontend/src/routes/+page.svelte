<script>
	import { Router, Route } from 'svelte-routing';
	import Home from '../components/Home.svelte';
	import MapCa from '../components/MapCA.svelte';
	import MapDe from '../components/MapDE.svelte';

	export let url = '';
</script>

<Router {url}>
	<div>
		<Route path="/"><Home /></Route>
		<Route path="/de"><MapDe /></Route>
		<Route path="/ca"><MapCa /></Route>
	</div>
</Router>
