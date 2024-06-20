from flask import Blueprint, render_template, session
from exercise_tracker import tracker


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    workouts = tracker.workouts_by_date()
    date = session.get('date')
    loaded = session.get('loaded', False)
    return render_template('index.html',
                           date=date,
                           workouts=workouts,
                           loaded=loaded)


@bp.route('/analysis')
def analysis():
    return render_template('analysis.html')
