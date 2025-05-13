from fastapi import APIRouter, Query
from app.repositories.SetRepository import SetRepository
from app.repositories.WorkoutRepository import WorkoutRepository
from app.schemas.exercise import LastExerciseDataResponse
from app.schemas.workout import SaveWorkout

router = APIRouter()


@router.get("/api/last_exercise_data", response_model=LastExerciseDataResponse)
def get_last_exercise_data(name: str = Query(...)):
    return SetRepository.get_last_exercise_data(name)


@router.post("/api/save_workout")
def saveWorkout(data: SaveWorkout):
    try:
        WorkoutRepository.save_workout(data)
        return {"success": True}
    except Exception as e:
        print(f"Error in save_workout: {e}")
        return {"success": False, "error": str(e)}
