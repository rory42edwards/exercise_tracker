from app.db.models import Set, Exercise, Workout
from app.db.db_local import SessionLocal
from datetime import date
from sqlalchemy import desc
from sqlalchemy.orm import joinedload


class SetRepository:

    @staticmethod
    def get_total_sets(workout_date: date) -> int:
        """Returns total number of sets in a workout.

        Args:
            workout_date (date): The date of the workout as a datetime.date object.

        Returns:
            int: The total number of sets in a workout on the given date.
        """
        session = SessionLocal()
        try:
            sets = session.query(Set)\
                    .join(Set.exercise)\
                    .join(Exercise.workout)\
                    .filter(Workout.date == workout_date)\
                    .all()
            return len(sets)
        finally:
            session.close()

    @staticmethod
    def get_sets_for_exercise_on_date(exercise_name: str, workout_date: date) -> list[Set]:
        """Returns a list of sets for an exercise on a given date.

        Args:
            exercise_name (str): The name of the exercise.
            workout_date (date): The datetime.date of the workout.

        Returns:
            list: A list of Set database objects.
        """
        session = SessionLocal()
        try:
            sets = (
                    session.query(Set)
                    .join(Set.exercise)
                    .join(Exercise.workout)
                    .filter(
                        Workout.date == workout_date,
                        Exercise.name == exercise_name
                    )
                    .order_by(Set.set_order.asc())
                    .all()
            )
            return sets
        finally:
            session.close()

    @staticmethod
    def delete(set_id: int) -> bool:
        session = SessionLocal()
        try:
            s = session.query(Set).filter(Set.id == set_id).first()
            if s:
                session.delete(s)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            print(f"Error deleting set: {e}")
        finally:
            session.close()

    @staticmethod
    def get_last_exercise_data(name: str):
        session = SessionLocal()
        try:
            exercise = (
                session.query(Exercise)
                .filter(Exercise.name == name)
                .join(Workout)
                .order_by(desc(Workout.date))
                .options(joinedload(Exercise.sets), joinedload(Exercise.workout))
                .first()
            )
            if exercise:
                return {
                    "date": exercise.workout.date.isoformat(),
                    "sets": [
                        {
                            "reps": s.reps,
                            "load": s.load,
                            "rpe": s.rpe
                        } for s in sorted(exercise.sets, key=lambda s: s.set_order)
                    ]
                }
            else:
                return {
                    "date": None,
                    "sets": []
                }
        finally:
            session.close()
