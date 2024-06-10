from datetime import datetime


class Exercise:
    def __init__(self, name, date):
        self.name = name
        self.sets = []
        self.date = date

    def add_set(self, reps):
        self.sets.append(reps)

    def to_dict(self):
        return {'name': self.name,
                'sets': self.sets,
                'date': self.date.isoformat()  # convert datetime to ISO string
                }

    @classmethod
    def from_dict(cls, data):
        exercise = cls(data['name'], datetime.fromisoformat(data['date']))
        exercise.sets = data['sets']
        return exercise

    def __str__(self):
        return f'{self.name}: {self.sets} on {self.date.strftime("%Y-%m-%d")}'
