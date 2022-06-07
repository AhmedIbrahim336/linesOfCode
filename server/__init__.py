import os

from flask import Flask, url_for

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
         SECRET_KEY='dev',
         DATABASE=os.path.join(app.instance_path, 'server.sqlite'),
         TEST_DATA=os.path.join(app.root_path, 'data/test_data.json')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, World!'
    # Commands 
    from . import db
    db.init_app(app)
    # Blue Prints 
    from . import project
    app.register_blueprint(project.bp)

    return app
