export function renderWorkouts(tracker) {
    const container = document.getElementById('workoutHistoryContainer');
    container.innerHTML = '';
    const sortedWorkouts = tracker.workoutsByDate();

    const header = document.createElement('h2');
    header.innerHTML = `Workouts`;
    container.appendChild(header);

    // create and add a save button
    const saveElement = document.createElement('div');
    const saveButton = document.createElement('button');
    saveButton.classList.add('btn', 'btn-primary', 'saveButton', 'mt-3');
    saveButton.setAttribute('data-action', 'saveTracker');
    saveButton.innerText = 'Save';
    saveElement.appendChild(saveButton);
    container.appendChild(saveElement);

    const workoutList = document.createElement('ul');
    workoutList.classList.add('list-group');
    sortedWorkouts.forEach(workout => {
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
        removeWorkoutButton.setAttribute('data-action', 'removeWorkout');
        removeWorkoutButton.innerText = 'Remove workout';
        removeWorkoutElement.appendChild(removeWorkoutButton);
        workoutElement.appendChild(removeWorkoutElement);


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
        });
    });
}
