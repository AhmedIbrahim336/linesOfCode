import functools
from flask import Blueprint, request, current_app
import json
from server.db import get_db

bp = Blueprint('projects', __name__, url_prefix='/projects')

@bp.route('/', methods=['GET'])
def get_projects():
    if request.method == 'GET':
        with current_app.open_resource(current_app.config['TEST_DATA']) as f:
            response = current_app.response_class(
                response=f.read().decode('utf-8'),
                status=200,
                mimetype='application/json'
            )
            return response
