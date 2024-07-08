from typing import Type
from exercise_tracker.set import Set


class Exercise:
    def __init__(self, name: str):
        self.name = name.lower().strip()
        self.sets: list[Set] = []

    def add_set(self, reps: int, load: float) -> None:
        sett = Set(reps, load)
        self.sets.append(sett)

    def to_dict(self) -> dict:
        return {'name': self.name,
                'sets': [sett.to_dict()
                         for sett in self.sets]
                }

    @classmethod
    def from_dict(cls: Type['Exercise'], data: dict) -> 'Exercise':
        exercise = cls(data['name'])
        exercise.sets = [Set.from_dict(sett) for
                         sett in data['sets']]
        return exercise

    def __str__(self):
        return f'{self.name}: {self.sets}'
