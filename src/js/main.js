import { Chart, registerables } from 'chart.js';
import 'chartjs-adapter-date-fns';

// Register all components
Chart.register(...registerables);

const canvasElement = document.getElementById('myChart');
const ctx = canvasElement.getContext('2d');

const myChart = new Chart(ctx, {
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

async function fetchExerciseLoadData(exerciseName) {
    const response = await fetch(`/api/exercise_load?name=${exerciseName}`);
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch exercise data');
    }
    const data = await response.json();
    return data;
}

async function fetchExerciseLoadVolumeData(exerciseName) {
    const response = await fetch(`/api/exercise_load_volume?name=${exerciseName}`);
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch exercise data');
    }
    const data = await response.json();
    return data;
}

function updateChart(data) {
    myChart.data.labels = data.labels;
    myChart.data.datasets[0].data = data.values;
    myChart.update();
}

document.querySelectorAll('.plot-load-button').forEach(button => {
    button.addEventListener('click', async (event) => {
        const exerciseName = event.target.getAttribute('data-exercise');
        const data = await fetchExerciseLoadData(exerciseName);
        console.log('Fetched data: ', data);
        updateChart(data);
    });
});

document.querySelectorAll('.plot-load-volume-button').forEach(button => {
    button.addEventListener('click', async (event) => {
        const exerciseName = event.target.getAttribute('data-exercise');
        const data = await fetchExerciseLoadVolumeData(exerciseName);
        console.log('Fetched data: ', data);
        updateChart(data);
    });
});
