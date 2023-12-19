<script>
	import { Link } from 'svelte-routing';
</script>

<div class="bg-gray-100 min-h-screen flex items-center justify-center">
	<div class="max-w-md mx-auto p-6 bg-white rounded shadow-md">
		<div class="text-3xl font-bold mb-4">BusSystem</div>
		<div class="text-xl mb-4">Team German</div>
		<div class="mb-6">
			<p>
				Monitor the traffic state at <span class="text-blue-500 font-bold">Canada</span> and
				<span class="text-blue-500 font-bold">Germany</span> with overview of bus route and traffic congestion
				prediction.
			</p>
		</div>
		<div class="space-y-4">
			<div>
				<Link to="de">
					<div
						class="bg-transparent border-2 border-blue-500 hover:bg-blue-500 hover:text-white text-blue-500 px-6 py-3 rounded transition duration-300 ease-in-out"
					>
						Deutsch
					</div>
				</Link>
			</div>
			<div>
				<Link to="ca">
					<div
						class="bg-transparent border-2 border-blue-500 hover:bg-blue-500 hover:text-white text-blue-500 px-6 py-3 rounded transition duration-300 ease-in-out"
					>
						Canada
					</div>
				</Link>
			</div>
		</div>
	</div>
</div>
