import { Workout } from '../modules/classes.js'
import { renderAddWorkoutForm } from '../modules/logWorkoutUI.js'
import { saveWorkoutState, loadWorkoutState } from '../modules/workoutState.js'
import { saveWorkout } from '../modules/workoutAPI.js'

function handleAction(type, payload, workout) {
    switch (type) {
        case 'addWorkout':
            workout.date = payload;
            break;
        
        case 'saveWorkout':
            console.log("saveWorkout payload", payload);
            saveWorkout(payload);
            return;
        
        case 'addExercise':
            workout.addExercise(payload.name);
            break;

        case 'addSet':
            workout.getExercise(payload.exercise).addSet(payload.reps, payload.load);
            break;

        case 'removeExercise':
            workout.removeExercise(payload.name);
            break;
    }

    saveWorkoutState(workout);
    renderAddWorkoutForm(workout);
}

async function init() {
    const saved = loadWorkoutState();
    const currentWorkout = saved || new Workout(new Date().toISOString().split('T')[0]);

    if (!saved) {
        saveWorkoutState(currentWorkout);
    }

    renderAddWorkoutForm(currentWorkout);

    document.getElementById('workoutFormContainer').addEventListener('click', (event) => {
        const button = event.target.closest('button');
        if (!button) return;

        const action = button.dataset.action;
        if (!action) return;

        switch (action) {
            case 'addWorkout': {
                console.log("adding workout");
                const newDate = document.getElementById('workoutDate').value;
                if (newDate) handleAction('addWorkout', newDate, currentWorkout);
                break;
            }

            case 'saveWorkout': {
                console.log("saving workout");
                console.log("currentWorkout", currentWorkout);
                handleAction('saveWorkout', currentWorkout, currentWorkout);
                break;
            }

            case 'addExercise': {
                console.log("adding exercise");
                const input = button.parentElement.querySelector('input[type="text"]');
                const exerciseName = input?.value;
                const date = button.dataset.date;
                if (exerciseName) handleAction('addExercise', { date, name: exerciseName }, currentWorkout);
                break;
            }

            case 'removeExercise': {
                console.log("removing exercise");
                handleAction('removeExercise', {
                    date: button.dataset.date,
                    name: button.dataset.exerciseName
                }, currentWorkout);
                break;
            }

            case 'addSet': {
                console.log("adding set");
                const reps = parseInt(button.parentElement.querySelector('input[placeholder="Reps"]').value);
                const load = parseFloat(button.parentElement.querySelector('input[placeholder^="Load"]').value);
                handleAction('addSet', {
                    date: button.dataset.date,
                    exercise: button.dataset.exercise,
                    reps,
                    load
                }, currentWorkout);
                break;
            }

            case 'saveAll': {
                console.log("saving workout");
                handleAction('saveAll', {}, currentWorkout);
                break;
            }

            default:
                console.warn('Unhandled action: ', action);
        }
    });
}

window.addEventListener('DOMContentLoaded', init);
