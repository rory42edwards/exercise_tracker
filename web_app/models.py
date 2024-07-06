from . import db


class Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movement_tags = db.relationship('MovementTag', backref='movement', cascade='all, delete-orphan')


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    movement_tags = db.relationship('MovementTag', backref='tag', cascade='all, delete-orphan')


class MovementTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movement_id = db.Column(db.Integer,
                            db.ForeignKey('movement.id'),
                            nullable=False)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey('tag.id'),
                       nullable=False)
    value = db.Column(db.String(100),
                      nullable=False)
