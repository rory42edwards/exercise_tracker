export async function fetchExerciseLoadData(exerciseName) {
    const response = await fetch(`/api/exercise_load?name=${exerciseName}`);
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch exercise data');
    }
    const data = await response.json();
    return data;
}

export async function fetchExerciseLoadVolumeData(exerciseName) {
    const response = await fetch(`/api/exercise_load_volume?name=${exerciseName}`);
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch exercise data');
    }
    const data = await response.json();
    return data;
}

export async function fetchProgressiveOverloadData(exerciseName) {
    const response = await fetch(`/api/exercise_prog_overload?name=${exerciseName}`);
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Failed to fetch exercise data');
    }
    const data = await response.json();
    return data;
}
