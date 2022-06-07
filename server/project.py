import functools
from flask import Blueprint, request, jsonify, url_for
from server.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/projects')

@bp.route('/', methods=['GET'])
def get_projects():
    if request.method == 'GET':
        return jsonify({})
