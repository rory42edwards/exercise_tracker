from flask import Blueprint, render_template, session, g
from exercise_tracker import tracker
from exercise_analysis import analyser


bp = Blueprint('main', __name__)


def load_tracker():
    if 'tracker' not in g:
        tracker.load_from_file('data/workouts.json')
        g.tracker = tracker


def load_analyser():
    if 'analyser' not in g:
        analyser.create_movements(g.tracker.workouts)
        g.analyser = analyser


@bp.before_request
def before_request():
    load_tracker()
    load_analyser()


@bp.route('/')
def index():
    workouts = g.tracker.workouts_by_date()
    date = session.get('date')
    loaded = session.get('loaded', False)
    return render_template('index.html',
                           date=date,
                           workouts=workouts,
                           loaded=loaded)


@bp.route('/analysis')
def analysis():
    movements = g.analyser.movements
    return render_template('analysis.html',
                           movements=movements)
