import os
from flask import Flask
from db.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_app(database_url=None):
    app = Flask(__name__, static_url_path='/static', static_folder='static')
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = 'bj69420'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if database_url is None:
        basedir = os.path.abspath(os.path.dirname(__file__))
        database_url = "sqlite:///" + os.path.join(basedir, "..", "data", "repdojo.db")
    engine = create_engine(database_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    app.session_local = sessionmaker(bind=engine)

    with app.app_context():
        from .routes import main

        app.register_blueprint(main.bp)

    return app
