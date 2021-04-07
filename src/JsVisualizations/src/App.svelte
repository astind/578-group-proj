<script lang="ts">
	import Papa from 'papaparse';
	import BarChart from './BarChart.svelte';
	let over50k = null, under50k = null;
	let loaded = false;

	fetch('./data/adult.data.csv').then(res => {
		return res.text();
	})
	.then(data => {
		const parsedData = Papa.parse(data, { header: true, delimiter: ', ' });
		over50k = [];
		under50k = [];
		parsedData.data.forEach(dataPoint => {
			if (dataPoint.income === '>50K') over50k.push(dataPoint);
			else under50k.push(dataPoint);
		});
		loaded = true;
	})
	.catch(console.log);
</script>

<main>
	{#if loaded}
		<BarChart {over50k} {under50k} />
	{/if}	
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 80%;
		margin: 0 auto;
	}
</style>