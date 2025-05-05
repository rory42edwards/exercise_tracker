from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Workout(Base):
    __tablename__ = 'workouts'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    title = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    exercises = relationship(
            "Exercise",
            back_populates="workout",
            cascade="all, delete-orphan"
    )
    supersets = relationship(
            "Superset",
            back_populates="workout",
            cascade="all, delete-orphan"
    )


class Superset(Base):
    __tablename__ = 'supersets'
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))

    workout = relationship("Workout", back_populates="supersets")
    exercises = relationship(
            "Exercise",
            back_populates="superset",
            cascade="all, delete-orphan"
    )


class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    superset_id = Column(Integer, ForeignKey('supersets.id'), nullable=True)
    name = Column(String, nullable=False)
    exercise_order = Column(Integer)

    workout = relationship("Workout", back_populates="exercises")
    superset = relationship("Superset", back_populates="exercises")
    sets = relationship(
            "Set",
            back_populates="exercise",
            cascade="all, delete-orphan"
    )


class Set(Base):
    __tablename__ = 'sets'
    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    reps = Column(Integer, nullable=False)
    load = Column(Float, nullable=False)
    rpe = Column(Integer, nullable=True)
    set_order = Column(Integer)

    exercise = relationship("Exercise", back_populates="sets")
