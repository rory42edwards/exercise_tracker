from typing import Type


class Exercise:
    def __init__(self, name: str):
        self.name = name
        self.sets: list[tuple] = []

    def add_set(self, reps: int, load: float) -> None:
        self.sets.append((reps, load))

    def to_dict(self) -> dict:
        return {'name': self.name,
                'sets': self.sets
                }

    @classmethod
    def from_dict(cls: Type['Exercise'], data: dict) -> 'Exercise':
        exercise = cls(data['name'])
        exercise.sets = data['sets']
        return exercise

    def __str__(self):
        return f'{self.name}: {self.sets}'
