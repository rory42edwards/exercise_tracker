from flask import Blueprint, g, send_file
from exercise_analysis import analyser
from exercise_tracker import tracker
import os


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
    if not movement:
        return f"Movement: {name} not found!"
    filepath = g.analyser.plot_load_over_time(movement)
    if filepath:
        return send_file(filepath, mimetype='image/png')
    else:
        return "Failed to generate plot", 500
