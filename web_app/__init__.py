from flask import Flask
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'bj69420'
    Session(app)

    with app.app_context():
        from .routes import main, exercises, workouts, analysis

        app.register_blueprint(main.bp)
        app.register_blueprint(exercises.bp)
        app.register_blueprint(workouts.bp)
        app.register_blueprint(analysis.bp)

    return app
