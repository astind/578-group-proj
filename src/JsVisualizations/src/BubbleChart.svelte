<script lang='ts'>
    import { onMount } from 'svelte';
    import { Chart, BubbleController, PointElement, CategoryScale, LinearScale, Title, Legend } from 'chart.js';
    import palette from './palette';
	import { columnLabelsMap, getCombinationCounts } from './dataCreation';
    import type { _DeepPartialObject } from 'chart.js/types/utils';
    export let counts = [];
    export let under50k;
    const selectionOptions = Object.keys(columnLabelsMap);
    let column1 = selectionOptions[0];
    let column2 = selectionOptions[1];

    let bubbleChart: Chart;

    const getOptions = (): unknown => {
        return {
            scales: {
                x: {
                    min: -1,
                    max: columnLabelsMap[column1].length,
                    type: 'linear',
                    ticks: {
                        stepSize: 1,
                        callback: (value: number) => {
                            return columnLabelsMap[column1][value] || '';
                        }
                    }
                },
                y: {
                    min: -1,
                    max: columnLabelsMap[column2].length,
                    type: 'linear',
                    ticks: {
                        stepSize: 1,
                        callback: (value: number) => {
                            return columnLabelsMap[column2][value] || '';
                        }
                    }
                }
            }
        }
    } 

    const getDataSets = () => {
        counts = getCombinationCounts(under50k, column1, column2);
        return [
            {
                label: `${column1} vs. ${column2}`,
                data: counts,
                backgroundColor: palette.blueTransparent,
                borderColor: palette.blue 
            }
        ];
    }
    
    const onSelectionChange = (e, columnNum) => {
        if (columnNum === 1) column1 = e.target.value;
        else column2 = e.target.value;
        
        bubbleChart.data = {
            datasets: getDataSets()
        }
        bubbleChart.options = getOptions()
        bubbleChart.update()
    }

    onMount(() => {
        Chart.register(BubbleController, PointElement, CategoryScale, LinearScale, Title, Legend);
        if (under50k) {
            const ctx = document.getElementById('bubble-chart') as HTMLCanvasElement;
            bubbleChart = new Chart(ctx.getContext('2d'), {
                type: 'bubble',
                data: {
                    datasets: getDataSets()
                },
                options: getOptions()
            });
        }
    });
</script>

<div>
    <canvas id='bubble-chart'></canvas>
    <div class="select-container">
        <!-- svelte-ignore a11y-no-onchange -->
        <select name='columns' id='columns' on:change={e => onSelectionChange(e, 1)} value={column1}>
            {#each selectionOptions as column}
                <option value={column}>{column}</option>
            {/each}
        </select>
        <!-- svelte-ignore a11y-no-onchange -->
        <select name='columns' id='columns' on:change={e => onSelectionChange(e, 2)} value={column2}>
            {#each selectionOptions as column}
                <option value={column}>{column}</option>
            {/each}
        </select>
    </div>
    
</div>

<style>
    div {
        margin-bottom: 1rem;
    }

    canvas {
        margin-bottom: .5rem;
    }
</style>