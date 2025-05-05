from db.models import Workout, Exercise, Set
from db.db_local import SessionLocal
from sqlalchemy.orm import joinedload
from datetime import date


class WorkoutRepository:

    @staticmethod
    def get_by_id(workout_id: int) -> Workout:
        """Returns a Workout database object from an id.

        Args:
            workout_id (int): The workout id of a Workout in the database.

        Returns:
            Workout: A Workout database object.
        """
        session = SessionLocal()
        try:
            workout = session.query(Workout)\
                .options(
                    joinedload(Workout.exercises).joinedload(Exercise.sets)
                )\
                .filter(Workout.id == workout_id)\
                .first()
            return workout
        finally:
            session.close()

    @staticmethod
    def delete(workout_id: int) -> bool:
        session = SessionLocal()
        try:
            workout = session.query(Workout).filter(Workout.id == workout_id).first()
            if workout:
                session.delete(workout)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            print(f"Error deleting workout: {e}")
            return False
        finally:
            session.close()

    @staticmethod
    def list_between_dates(start_date: date, end_date: date) -> list[Workout]:
        if not isinstance(start_date, date) or not isinstance(end_date, date):
            raise TypeError(f"Input dates must be datetime.date objects.\nCurrently types are: start_date {type(start_date)}, end_date {type(end_date)}")
        session = SessionLocal()
        try:
            workouts = session.query(Workout)\
                .filter(Workout.date >= start_date, Workout.date <= end_date)\
                .order_by(Workout.date.desc())\
                .all()
            return workouts
        finally:
            session.close()
#  .options(joinedload(Workout.exercises).joinedload(Exercise.sets))\
