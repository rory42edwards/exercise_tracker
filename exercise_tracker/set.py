from typing import Type


class Set:
    def __init__(self, reps: int, load: float):
        self.reps = int(reps)
        self.load = float(load)

    def to_dict(self) -> dict:
        return {'reps': self.reps,
                'load': self.load
                }

    @classmethod
    def from_dict(cls: Type['Set'], data: dict) -> 'Set':
        sett = cls(data['reps'], data['load'])
        return sett

    def __str__(self):
        return f'Reps: {self.reps}, Load: {self.load}'
