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
