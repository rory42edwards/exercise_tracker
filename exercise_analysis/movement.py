class Movement:
    """
    The Movement class is for analysis as a way to combine\
    multiple exercises from multiple dates into one object
    """

    def __init__(self, name):
        self.name = name
        self.all_sets = {}

    def add_workout(self, date, sets):
        self.all_sets.update({date: sets})

    def __str__(self):
        return f'{self.name}: {self.all_sets}'
