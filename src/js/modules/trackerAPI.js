export async function saveTracker(data) {
    const response = await fetch('/save_tracker', {
        method: 'post',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

export async function fetchData() {
    try {
        const response = await fetch('/api/get_data');
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    } catch (error) {
            console.error('Problem with fetch operation: ', error);
        }
}
