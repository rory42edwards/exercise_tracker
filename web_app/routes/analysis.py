from flask import Blueprint, redirect, url_for, g
from exercise_analysis import analyser
from exercise_tracker import tracker


bp = Blueprint('analysis', __name__)


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


@bp.route('/plot_movement_load/<name>', methods=['POST'])
def plot_movement_load(name):
    movement = g.analyser.get_movement(name)
    g.analyser.plot_load_over_time(movement)
    return redirect(url_for('main.analysis'))
