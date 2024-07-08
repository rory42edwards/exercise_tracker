from flask import Blueprint, request, url_for, redirect
from flask.json import jsonify
from web_app.models import Movement, Tag, MovementTag
from web_app import db

bp = Blueprint('database', __name__)


@bp.route('/add_movement', methods=['POST'])
def add_movement():
    name = request.form['name'].lower().strip()
    if not name:
        return 'Name is required', 400
    movement = Movement(name=name)
    db.session.add(movement)
    try:
        db.session.commit()
        return 'Movement added', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 500


@bp.route('/delete_movement', methods=['POST'])
def delete_movement():
    try:
        data = request.get_json()
        print(data)
        movement_id = data.get('movement_id')
        if not movement_id:
            return 'Movement ID is required', 400
        movement = Movement.query.get(movement_id)
        db.session.delete(movement)
        db.session.commit()
        return 'Movement deleted', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 500


@bp.route('/add_tag', methods=['POST'])
def add_tag():
    name = request.form['name'].lower().strip()
    if not name:
        return 'Name is required', 400
    tag = Tag(name=name)
    db.session.add(tag)
    try:
        db.session.commit()
        return 'Tag added', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 500


@bp.route('/delete_tag', methods=['POST'])
def delete_tag():
    try:
        data = request.get_json()
        tag_id = data.get('tag_id')
        if not tag_id:
            return 'Tag ID is required', 400
        tag = Tag.query.get(tag_id)
        db.session.delete(tag)
        db.session.commit()
        return 'Tag deleted', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 500


@bp.route('/add_movement_tag', methods=['POST'])
def add_movement_tag():
    try:
        data = request.get_json()
        print(data)
        movement_id = data.get('movement_id')
        tag_id = data.get('tag_id')
        value = data.get('value')
        if not movement_id or not tag_id or not value:
            return jsonify({'success': False, 'message': 'Movement ID, Tag ID, and Value are required'}), 400
        movement_tag = MovementTag(movement_id=movement_id,
                                   tag_id=tag_id,
                                   value=value)
        db.session.add(movement_tag)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Movement tag added'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@bp.route('/delete_movement_tag', methods=['POST'])
def delete_movement_tag():
    try:
        data = request.get_json()
        print(data)
        movement_id = data.get('movement_id')
        tag_id = data.get('tag_id')
        value = data.get('value')
        if not movement_id or not tag_id or not value:
            return jsonify({'success': False, 'message': 'Movement ID, Tag ID, and Value are required'}), 400
        movement_tag = MovementTag(movement_id=movement_id,
                                   tag_id=tag_id,
                                   value=value)
        db.session.add(movement_tag)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Movement tag added'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 500


@bp.route('/get_movements', methods=['GET'])
def get_movements():
    try:
        movements = Movement.query.all()
        results = []
        for movement in movements:
            tags = {mt.tag.name: mt.value for mt in movement.movement_tags}
            results.append({'name': movement.name, 'tags': tags})
        return f'{results}', 200
    except Exception as e:
        db.session.rollback()
        return str(e), 500
