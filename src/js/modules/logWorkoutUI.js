export function renderAddWorkoutForm(workout) {
    const container = document.getElementById('workoutFormContainer');
    container.innerHTML = '';

    const header = document.createElement('h2');
    header.innerHTML = `Add Workout`;
    container.appendChild(header);

    // create and add a save button
    const saveElement = document.createElement('div');
    const saveButton = document.createElement('button');
    saveButton.classList.add('btn', 'btn-primary', 'saveButton', 'mt-3');
    saveButton.setAttribute('data-action', 'saveWorkout');
    saveButton.innerText = 'Save Workout';
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
    addWorkoutButton.setAttribute('data-action', 'addWorkout');
    addWorkoutButton.innerText = 'New workout';
    addWorkoutElement.appendChild(addWorkoutInput);
    addWorkoutElement.appendChild(addWorkoutButton);
    container.appendChild(addWorkoutElement);

    const workoutElement = document.createElement('li');
    workoutElement.classList.add('list-group-item');
    if (workout.date) {
        if (workout.date.length > 11) {
            const date = workout.date.slice(0, -9);
            workoutElement.innerHTML = `<strong>${date}</strong>`;
        }
        else {
            workoutElement.innerHTML = `<strong>${workout.date}</strong>`;
        }
    }

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
    addExerciseButton.setAttribute('data-action', 'addExercise');
    addExerciseButton.innerText = 'Add Exercise';
    addExerciseElement.appendChild(exerciseInput);
    addExerciseElement.appendChild(addExerciseButton);
    workoutElement.appendChild(addExerciseElement);

    container.appendChild(workoutElement);

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
        removeExerciseButton.setAttribute('data-action', 'removeExercise');
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
        addSetButton.setAttribute('data-action', 'addSet');
        addSetButton.innerText = 'Add Set';

        addSetElement.appendChild(repsInput);
        addSetElement.appendChild(loadInput);
        addSetElement.appendChild(addSetButton);
        exerciseElement.appendChild(addSetElement);
    });

}
