from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'bj69420'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movements.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Session(app)
    db.init_app(app)

    with app.app_context():
        from .routes import main, exercises, workouts, analysis_api, sql
        from .models import Movement, Tag, MovementTag

        app.register_blueprint(main.bp)
        app.register_blueprint(exercises.bp)
        app.register_blueprint(workouts.bp)
        app.register_blueprint(analysis_api.bp)
        app.register_blueprint(sql.bp)

        db.create_all()

    return app
