export async function saveWorkout(data) {
    const response = await fetch('/save_workout', {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

export async function fetchLastExerciseData(exerciseName) {
    try {
        const response = await fetch(`http://localhost:8000/api/last_exercise_data?name=${encodeURIComponent(exerciseName)}`);
        if (!response.ok) {
            throw new Error("API request failed");
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching last exercise data: ", error);
        return null;
    }
}
