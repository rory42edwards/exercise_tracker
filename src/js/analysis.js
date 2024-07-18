import { fetchExerciseLoadData, fetchExerciseLoadVolumeData, fetchProgressiveOverloadData } from './api.js';
import { updateChart, createTimeChart } from './mychart.js';
import { renderMovements } from './analysisDOM.js';

const pythonMovements = window.pythonMovements;

renderMovements();
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/get_movements')
        .then(response => response.json())
        .then(movementData => {
            const mergedData = pythonMovements.map(pm => {
                const match = movementData.find(md => md.id === pm.id);
                return {
                    ...pm,
                    tags: match ? match.tags : {}
                };
            });

            console.log(mergedData);
        });

    document.getElementById('movementForm').addEventListener('submit', async (event) => {
        event.preventDefault();
        const movementSelect = document.getElementById('movementId');
        const selectedOption = movementSelect.options[movementSelect.selectedIndex];
        const exerciseName = selectedOption.getAttribute('data-exercise');
        const data = await fetchExerciseLoadData(exerciseName);
        console.log('Fetched data: ', data);
        const container = document.getElementById('analysisContainer');
        const existingCanvas = document.getElementById('myChart');

        if (existingCanvas) {
            existingCanvas.remove();
        }

        const canvasElement = document.createElement('canvas');
        canvasElement.setAttribute('id', 'myChart');
        canvasElement.setAttribute('height', '200');
        canvasElement.setAttribute('width', '400');
        container.appendChild(canvasElement);

        const chart = createTimeChart();
        updateChart(chart,data);
    });

    document.querySelectorAll('.plot-load-button').forEach(button => {
        button.addEventListener('click', async (event) => {
            const exerciseName = event.target.getAttribute('data-exercise');
            console.log(exerciseName);
            const data = await fetchExerciseLoadData(exerciseName);
            console.log('Fetched data: ', data);

            const container = document.getElementById('analysisContainer');
            const existingCanvas = document.getElementById('myChart');

            if (existingCanvas) {
                existingCanvas.remove();
            }

            const canvasElement = document.createElement('canvas');
            canvasElement.setAttribute('id', 'myChart');
            canvasElement.setAttribute('height', '200');
            canvasElement.setAttribute('width', '400');
            container.appendChild(canvasElement);

            const chart = createTimeChart();
            updateChart(chart,data);
        });
    });

    document.querySelectorAll('.plot-load-volume-button').forEach(button => {
        button.addEventListener('click', async (event) => {
            const exerciseName = event.target.getAttribute('data-exercise');
            const data = await fetchExerciseLoadVolumeData(exerciseName);
            console.log('Fetched data: ', data);
            const chart = createTimeChart();
            updateChart(chart,data);
        });
    });

    document.querySelectorAll('.plot-prog-overload').forEach(button => {
        button.addEventListener('click', async (event) => {
            const exerciseName = event.target.getAttribute('data-exercise');
            const data = await fetchProgressiveOverloadData(exerciseName);
            console.log('Fetched data: ', data);
            const chart = createTimeChart();
            updateChart(chart,data);
        });
    });
});
