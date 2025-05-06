from fastapi import APIRouter, Query
from app.repositories.SetRepository import SetRepository
from app.schemas.exercise import LastExerciseDataResponse

router = APIRouter()


@router.get("/api/last_exercise_data", response_model=LastExerciseDataResponse)
def get_last_exercise_data(name: str = Query(...)):
    return SetRepository.get_last_exercise_data(name)
