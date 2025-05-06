from pydantic import BaseModel
from typing import List, Optional


class SetData(BaseModel):
    reps: int
    load: float
    rpe: Optional[float]


class LastExerciseDataResponse(BaseModel):
    date: Optional[str]
    sets: List[SetData]
