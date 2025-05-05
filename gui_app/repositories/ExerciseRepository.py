from db.models import Workout, Exercise, Set
from db.db_local import SessionLocal
from sqlalchemy.orm import joinedload


class ExerciseRepository:

    @staticmethod
    def get_exercises(workout_id: int) -> list[Exercise]:
        """Returns a list of exercise objects from a given workout id.

        Args:
            workout_id (int): The workout id of a Workout in the database.

        Returns:
            list: A list of Exercise database objects.
        """
        session = SessionLocal()
        try:
            exercises = (
                    session.query(Exercise)
                    .options(joinedload(Exercise.sets))
                    .filter(Exercise.workout_id == workout_id)
                    .order_by(Exercise.exercise_order.asc())
                    .all()
            )

            return exercises

        finally:
            session.close()

    @staticmethod
    def add(workout_id: int, name: str) -> bool:
        """Adds an exercise to a workout.

        Args:
            workout_id (int): The id of a workout in the database.
            name (str): The name of the exercise.

        Returns:
            bool: True for success, False for failed to add.
        """
        session = SessionLocal()
        try:
            ...
        finally:
            session.close()

    @staticmethod
    def delete(workout_id: int) -> bool:
        """Deletes an exercise from a workout.

        Args:
            workout_id (int): The id of a workout in the database.

        Returns:
            bool: True for success, False otherwise.
        """
        session = SessionLocal()
        try:
            ...
        finally:
            session.close()

    def find(name: str) -> list[Exercise]:
        """Finds an exercise with a given name.

        Args:
            name (str): Name of the exercise.

        Returns:
            list: A list of Exercise db objects with the given name.
        """
        session = SessionLocal()
        try:
            results = session.query(Exercise)\
                    .options(joinedload(Exercise.sets))\
                    .filter(Exercise.name == name)\
                    .all()
            return results
        finally:
            session.close()

    def get_all_exercise_names() -> list[str]:
        """Gets all the exercise names.

        Returns:
            list: A list of all unique names of exercises in the database.
        """
        session = SessionLocal()
        try:
            results = session.query(Exercise.name).distinct().all()
            return [r[0] for r in results]
        finally:
            session.close()
