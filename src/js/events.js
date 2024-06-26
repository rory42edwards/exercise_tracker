import { fetchExerciseLoadData, fetchExerciseLoadVolumeData } from './api.js';
import { updateChart } from './dom.js';

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
