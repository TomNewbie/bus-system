/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			height: {
				'1/8': '10.5%',
				'9/10': '90%'
			}
		}
	},
	plugins: []
};
