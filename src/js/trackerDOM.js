import { Tracker } from './tracker.js';

let trackerState = null;

export function saveState(tracker) {
    localStorage.setItem('trackerState', JSON.stringify(tracker.workouts));
}

export function loadState() {
    const savedState = localStorage.getItem('trackerState');
    if (savedState) {
        trackerState = new Tracker();
        trackerState.loadWorkouts(JSON.parse(savedState));
        renderWorkouts(trackerState);
        return trackerState;
    }
    return null;
}

export function renderWorkouts(tracker) {
    const container = document.getElementById('workoutsContainer');
    container.innerHTML = '';
    const sortedWorkouts = tracker.workoutsByDate();

    const header = document.createElement('h2');
    header.innerHTML = `Workouts`;
    container.appendChild(header);

    // create and add a save button
    const saveElement = document.createElement('div');
    const saveButton = document.createElement('button');
    saveButton.classList.add('btn', 'btn-primary', 'saveButton', 'mt-3');
    saveButton.setAttribute('id', 'saveButton');
    saveButton.innerText = 'Save';
    saveElement.appendChild(saveButton);
    container.appendChild(saveElement);

    // create and add an add workout button
    const addWorkoutElement = document.createElement('div');
    addWorkoutElement.classList.add('mt-3');
    const addWorkoutInput = document.createElement('input');
    addWorkoutInput.type = 'date';
    addWorkoutInput.classList.add('form-control', 'd-inline-block', 'w-auto');
    addWorkoutInput.setAttribute('id', 'workoutDate');

    const addWorkoutButton = document.createElement('button');
    addWorkoutButton.classList.add('btn', 'btn-primary');
    addWorkoutButton.setAttribute('id', 'addWorkoutButton');
    addWorkoutButton.innerText = 'New workout';
    addWorkoutElement.appendChild(addWorkoutInput);
    addWorkoutElement.appendChild(addWorkoutButton);
    container.appendChild(addWorkoutElement);

    const workoutList = document.createElement('ul');
    workoutList.classList.add('list-group');
    sortedWorkouts.forEach(workout => {
        //const workoutElement = document.createElement('div');
        const workoutElement = document.createElement('li');
        workoutElement.classList.add('list-group-item');
        if (workout.date.length > 11) {
            const date = workout.date.slice(0, -9);
            workoutElement.innerHTML = `<strong>${date}</strong>`;
        }
        else {
            workoutElement.innerHTML = `<strong>${workout.date}</strong>`;
        }

        // create and add a delete workout button
        const removeWorkoutElement = document.createElement('div');
        const removeWorkoutButton = document.createElement('button');
        removeWorkoutButton.classList.add('btn', 'btn-danger', 'removeWorkoutButton', 'mb-2');
        removeWorkoutButton.setAttribute('data-date', workout.date);
        removeWorkoutButton.innerText = 'Remove workout';
        removeWorkoutElement.appendChild(removeWorkoutButton);
        workoutElement.appendChild(removeWorkoutElement);

        // create and add an add exercise button
        const addExerciseElement = document.createElement('div');
        addExerciseElement.classList.add('mt-3');
        const exerciseInput = document.createElement('input');
        exerciseInput.type = 'text';
        exerciseInput.placeholder = 'Exercise name';
        exerciseInput.classList.add('form-control', 'd-inline-block', 'w-auto');

        const addExerciseButton = document.createElement('button');
        addExerciseButton.classList.add('btn', 'btn-secondary', 'addExerciseButton');
        addExerciseButton.setAttribute('data-date', workout.date);
        addExerciseButton.innerText = 'Add Exercise';
        addExerciseElement.appendChild(exerciseInput);
        addExerciseElement.appendChild(addExerciseButton);
        workoutElement.appendChild(addExerciseElement);

        //container.appendChild(workoutElement);
        workoutList.appendChild(workoutElement);
        container.appendChild(workoutList);

        workout.exercises.slice().reverse().forEach(exercise => {
            const exerciseElement = document.createElement('div');
            exerciseElement.innerHTML = `<strong>${exercise.name}</strong>`;

            exercise.sets.forEach(set => {
                const setElement = document.createElement('div');
                setElement.innerText = `${set.reps} reps @ ${set.load} kg`;
                exerciseElement.appendChild(setElement);
            });

            workoutElement.appendChild(exerciseElement);

            // create and add a delete exercise button
            const removeExerciseElement = document.createElement('div');
            const removeExerciseButton = document.createElement('button');
            removeExerciseButton.classList.add('btn', 'btn-danger', 'removeExerciseButton');
            removeExerciseButton.setAttribute('data-date', workout.date);
            removeExerciseButton.setAttribute('data-exercise-name', exercise.name);
            removeExerciseButton.innerText = 'Remove exercise';
            removeExerciseElement.appendChild(removeExerciseButton);
            workoutElement.appendChild(removeExerciseElement);


            // create and add an add set button
            const addSetElement = document.createElement('div');

            const repsInput = document.createElement('input');
            repsInput.type = 'number';
            repsInput.placeholder = 'Reps';
            repsInput.classList.add('form-control', 'd-inline-block', 'w-auto');

            const loadInput = document.createElement('input');
            loadInput.type = 'number';
            loadInput.placeholder = 'Load (kg) -- 0 if bw';
            loadInput.classList.add('form-control', 'd-inline-block', 'w-auto');

            const addSetButton = document.createElement('button');
            addSetButton.classList.add('btn', 'btn-secondary', 'addSetButton', 'mb-2');
            addSetButton.setAttribute('data-date', workout.date);
            addSetButton.setAttribute('data-exercise', exercise.name);
            addSetButton.innerText = 'Add Set';

            addSetElement.appendChild(repsInput);
            addSetElement.appendChild(loadInput);
            addSetElement.appendChild(addSetButton);
            exerciseElement.appendChild(addSetElement);
        });
    });

    // Reattach event listeners after rendering
    document.getElementById('addWorkoutButton').addEventListener('click', () => {
        console.log("Trying to add workout");
        const date = document.getElementById('workoutDate').value;
        if (date){
            tracker.addWorkout(date);
            renderWorkouts(tracker);
            saveState(tracker);
        }
    });

    document.querySelectorAll('.addExerciseButton').forEach(button => {
        button.addEventListener('click', (event) => {
            console.log("Trying to add exercise");
            const date = event.target.getAttribute('data-date');
            const exerciseName = event.target.previousSibling.value;

            if (exerciseName) {
                const workout = tracker.getWorkout(date)
                workout.addExercise(exerciseName);
                renderWorkouts(tracker);
                saveState(tracker);
            }
        });
    });

    document.querySelectorAll('.addSetButton').forEach(button => {
        button.addEventListener('click', (event) => {
            console.log("Trying to add set");
            const date = event.target.getAttribute('data-date');
            const exerciseName = event.target.getAttribute('data-exercise');
            const repsInput = event.target.previousSibling.previousSibling;
            const loadInput = event.target.previousSibling;

            const reps = parseInt(repsInput.value);
            const load = parseFloat(loadInput.value);

            if (!isNaN(reps) && !isNaN(load)) {
                const workout = tracker.getWorkout(date);
                const exercise = workout.getExercise(exerciseName);
                exercise.addSet(reps, load);
                renderWorkouts(tracker);
                saveState(tracker);
            }
        });
    });

    document.getElementById('saveButton').addEventListener('click', () => {
        console.log("trying to save");
        fetch('/save', {
            method: 'post',
            headers: {
                'content-type': 'application/json'
            },
            body: JSON.stringify(tracker.workouts)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('data saved successfully');
            } else {
                alert('failed to save data');
            }
        });
    });

    document.querySelectorAll('.removeExerciseButton').forEach(button => {
        button.addEventListener('click', (event) => {
            console.log("trying to remove exercise");
            const date = event.target.getAttribute('data-date');
            const name = event.target.getAttribute('data-exercise-name');
            const workout = tracker.getWorkout(date);
            workout.removeExercise(name);
            renderWorkouts(tracker);
            saveState(tracker);
        });
    });

    document.querySelectorAll('.removeWorkoutButton').forEach(button => {
        button.addEventListener('click', (event) => {
            console.log("trying to remove workout");
            const date = event.target.getAttribute('data-date');
            tracker.removeWorkout(date);
            renderWorkouts(tracker);
            saveState(tracker);
        });
    });
}
