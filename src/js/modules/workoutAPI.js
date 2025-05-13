import { apiBaseUrl } from '../modules/apiURL.js'

export async function saveWorkout(data) {
    const response = await fetch(apiBaseUrl+'/save_workout', {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify({workout: data})
    });
    console.log(JSON.stringify({workout: data}))

    if (!response.ok) {
        throw new Error('Failed to save workout');
    }
    return await response.json();
}

export async function fetchLastExerciseData(exerciseName) {
    try {
        const response = await fetch(apiBaseUrl+`/last_exercise_data?name=${encodeURIComponent(exerciseName)}`);
        if (!response.ok) {
            throw new Error("API request failed");
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching last exercise data: ", error);
        return null;
    }
}
