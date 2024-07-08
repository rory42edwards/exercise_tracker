from datetime import datetime
from exercise_tracker.set import Set
import json


class Movement:
    """
    The Movement class is for analysis as a way to combine\
    multiple exercises from multiple dates into one object
    """

    def __init__(self, name: str):
        self.name = name.lower()
        self.all_sets: dict = {}

    def add_workout(self, date: datetime, sets: list['Set']) -> None:
        self.all_sets.update({date.isoformat(): sets})

    def __str__(self):
        return f'{self.name}: {self.all_sets}'

    def to_dict(self) -> dict:
        all_sets_dict: dict = {}
        for items in self.all_sets.items():
            all_sets_dict.update({items[0]:
                                 [sett.to_dict() for sett in items[1]]})
        return {'name': self.name,
                'all sets': all_sets_dict
                }
