import { Workout } from '../modules/classes.js'
import { renderAddWorkoutForm } from '../modules/logWorkoutUI.js'
import { saveWorkoutState, loadWorkoutState } from '../modules/workoutState.js'
import { saveWorkout, fetchLastExerciseData } from '../modules/workoutAPI.js'

async function handleAction(type, payload, workout) {
    switch (type) {
        case 'addWorkoutTitle':
            workout.title = payload;
            break;
        
        case 'addWorkoutDate':
            workout.date = payload;
            break;

        case 'saveWorkout':
            if (!workout.date) {
                alert('Please enter a date before saving a workout.');
                break;
            }
            if (!workout.title) {
                alert('Please enter a title before saving a workout.');
                break;
            }
            console.log("saveWorkout payload", payload);
            try {
                const result = await saveWorkout(payload);
                console.log(result.success);
                if (result.success) {
                    alert('Workout saved to database.');
                } else {
                    alert('Error saving workout: ' + (result.error || 'Unknown error'));
                }
            } catch (err) {
                console.error(err);
                alert('Failed to save workout. Network or server error.');
            }
            return;
        
        case 'addExercise':
            workout.addExercise(payload.name);
            break;

        case 'addSet':
            workout.getExercise(payload.exercise).addSet(payload.reps, payload.load, payload.rpe);
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
            case 'addWorkoutTitle': {
                console.log("adding workout title");
                const title = document.getElementById('workoutTitle').value;
                if (!title) break;
                handleAction('addWorkoutTitle', title, currentWorkout);
                break;
            }

            case 'addWorkoutDate': {
                console.log("adding workout date");
                const newDate = document.getElementById('workoutDate').value;
                if (!newDate) break;
                handleAction('addWorkoutDate', newDate, currentWorkout);
                break;
            }

            case 'clearLocalWorkout': {
                console.log("clearing local workout data");
                const confirmed = confirm("Are you sure you want to clear your saved workout?");
                if (confirmed) {
                    localStorage.removeItem('workoutState');
                    alert('Saved workout cleared.');
                    window.location.reload();
                    break;
                } else break;
            }

            case 'saveWorkout': {
                console.log("saving workout");
                console.log("currentWorkout", currentWorkout);
                handleAction('saveWorkout', currentWorkout, currentWorkout);
                break;
            }

            case 'addExercise': {
                addExercise(button, currentWorkout)
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
                const rpe = parseInt(button.parentElement.querySelector('input[placeholder="RPE"]').value);
                handleAction('addSet', {
                    date: button.dataset.date,
                    exercise: button.dataset.exercise,
                    reps,
                    load,
                    rpe
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
async function addExercise(button, currentWorkout) {
    console.log("adding exercise");
    const input = button.parentElement.querySelector('input[type="text"]');
    const exerciseName = input?.value;
    const date = button.dataset.date;
    if (exerciseName) {
        handleAction('addExercise', { date, name: exerciseName }, currentWorkout)
        // fetch last session data
        const last = await fetchLastExerciseData(exerciseName);
        if (last && last.sets.length > 0) {
            const msg = `Last time (${last.date}): ` + last.sets.map(s => `${s.reps}x${s.load}kg @ RPE ${s.rpe ?? '-'}`
            ).join(', ');
            const exerciseElement = document.querySelector(`[data-exercise="${exerciseName}"]`);
            if (exerciseElement) {
                const lastSessionInfo = document.createElement('div');
                lastSessionInfo.classList.add('text-muted', 'small');
                lastSessionInfo.innerText = msg;
                exerciseElement.appendChild(lastSessionInfo);
            } else {
                alert(msg);
            }
        } else {
            const msg = `No previous exercise data found.`;
            const exerciseElement = document.querySelector(`[data-exercise="${exerciseName}"]`);
            if (exerciseElement) {
                const lastSessionInfo = document.createElement('div');
                lastSessionInfo.classList.add('text-muted', 'small');
                lastSessionInfo.innerText = msg;
                exerciseElement.appendChild(lastSessionInfo);
            } else {
                alert(msg);
            }
        }
    }
}
