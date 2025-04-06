from . import db


class Movement(db.Model):
    __tablename__ = 'movements'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    movement_tags = db.relationship('MovementTag', back_populates='movement')


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    movement_tags = db.relationship('MovementTag', back_populates='tag')


class MovementTag(db.Model):
    __tablename__ = 'movement_tags'
    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movements.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
    value = db.Column(db.String(100))

    movement = db.relationship('Movement', back_populates='movement_tags')
    tag = db.relationship('Tag', back_populates='movement_tags')


class Workout(db.Model):
    __tablename__ = 'workouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False)  # e.g., 'YYYY-MM-DD'
    movement_id = db.Column(db.Integer, db.ForeignKey('movements.id'), nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float)

    movement = db.relationship('Movement')
