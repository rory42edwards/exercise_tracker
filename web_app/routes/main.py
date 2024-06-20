from flask import Blueprint, render_template, session, g
from exercise_tracker import tracker


bp = Blueprint('main', __name__)


def load_tracker():
    if 'tracker' not in g:
        tracker.load_from_file('data/workouts.json')
        g.tracker = tracker


@bp.before_request
def before_request():
    load_tracker()


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
    return render_template('analysis.html')
