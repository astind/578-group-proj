<script lang='ts'>
    import { onMount } from 'svelte';
    import { Chart, RadarController, RadialLinearScale, PointElement, LineElement, CategoryScale, LinearScale, Title, Legend } from 'chart.js';
    import palette from './palette';
	import { getCountsDataMap } from './dataCreation';
    export let countsDataMap = {};
    export let under50k;
    export let over50k;

    let barChart: Chart;

    const getOptions = (title?: string) => {
        return {
            plugins: {
                title: {
                    display: true,
                    text: `${title || 'Occupation'} totals`
                }
            }
        }
    };

    const getDataSets = (under50k, over50k) => {
        return [
            {
                label: 'Under 50k',
                fill: true,
                backgroundColor: palette.blueTransparent,
                borderColor: palette.blue,
                borderWidth: 3,
                pointBackgroundColor: palette.blueTransparent,
                data: under50k,
            },
            {
                label: 'Over 50k',
                fill: true,
                backgroundColor: palette.pinkTransparent,
                borderColor: palette.pink,
                borderWidth: 3,
                pointBackgroundColor: palette.pinkTransparent,
                data: over50k,
            }
        ];
    }

    const onSelectionChange = (e) => {
        const column = e.target.value;
        const c = countsDataMap[column];
        if (c) {
            const { under50k, over50k } = c.getData();
            barChart.data = {
                labels: c.labels,
                datasets: getDataSets(under50k, over50k)
            }
            barChart.options = getOptions(column);
            barChart.update()
        }
    }

    onMount(() => {
        Chart.register(RadarController, RadialLinearScale, PointElement, LineElement, CategoryScale, LinearScale, Title, Legend);
        if (under50k && over50k) {
            countsDataMap = getCountsDataMap(under50k, over50k);
            const { under50k: occupationUnder50k, over50k: occupationOver50k } = countsDataMap['occupation'].getData();
            const ctx = document.getElementById('radar-chart') as HTMLCanvasElement;
            console.log(ctx);
            barChart = new Chart(ctx.getContext('2d'), {
                type: 'radar',
                data: {
                    labels: countsDataMap['occupation'].labels,
                    datasets: getDataSets(occupationUnder50k, occupationOver50k)
                },
                options: getOptions()
            });
        }
    });
</script>

<div>
    <canvas id='radar-chart'></canvas>
    <!-- svelte-ignore a11y-no-onchange -->
    <select name='columns' id='columns' on:change={onSelectionChange} value="occupation">
        {#each Object.keys(countsDataMap) as column}
            <option value={column}>{column}</option>
        {/each}
    </select>
</div>

<style>
    div {
        margin-bottom: 1rem;
    }

    canvas {
        margin-bottom: .5rem;
    }
</style>