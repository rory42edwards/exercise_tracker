import { myChart } from './mychart.js';

export function updateChart(data) {
    myChart.data.labels = data.labels;
    myChart.data.datasets[0].data = data.values;
    myChart.update();
}
