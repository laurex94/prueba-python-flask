from flask import jsonify
from app.main import bp


@bp.route('/')
def index():
    return jsonify({'main':'main'})
