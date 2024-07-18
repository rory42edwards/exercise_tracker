import { Chart, registerables } from 'chart.js';
import 'chartjs-adapter-date-fns';

export function createTimeChart(){
    // Register all components
    Chart.register(...registerables);

    const canvasElement = document.getElementById('myChart');
    const ctx = canvasElement.getContext('2d');

    // create new chart
    const timeChart = new Chart(ctx, {
      type: 'scatter',
      data: {
        labels: [], // initialise with empty data
        datasets: [{
          label: 'Exercise Load Over Time',
          data: [],
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          fill: false,
          data: [] // initialise with empty data
        }]
      },
      options: {
        scales: {
          x: {
            type: 'time',
            time: {
              unit: 'day'
            }
          },
          y: {
            beginAtZero: false
          }
        }
      }
    });
    return timeChart;
} 

export function updateChart(chart,data) {
    console.log(data.labels);
    console.log(data.values);
    chart.data.labels = data.labels;
    chart.data.datasets[0].data = data.values;
    chart.update();
}
