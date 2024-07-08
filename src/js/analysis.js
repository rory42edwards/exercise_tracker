import { fetchExerciseLoadData, fetchExerciseLoadVolumeData } from './api.js';
import { updateChart } from './mychart.js';

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

const pythonMovements = window.pythonMovements;

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
});
