class Movement:
    """
    The Movement class is for analysis as a way to combine\
    multiple exercises from multiple dates into one object
    """

    def __init__(self, name: str):
        self.name = name
        self.all_sets: dict = {}

    def add_workout(self, date, sets) -> None:
        self.all_sets.update({date: sets})

    def __str__(self):
        return f'{self.name}: {self.all_sets}'
