from pydantic import BaseModel
from typing import List, Optional
from app.schemas.exercise import SetData


class ExerciseData(BaseModel):
    sets: List[SetData] = []
    name: str


class WorkoutData(BaseModel):
    exercises: List[ExerciseData]
    title: str
    notes: Optional[str]
    date: str


class SaveWorkout(BaseModel):
    workout: WorkoutData
