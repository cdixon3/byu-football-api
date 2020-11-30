import logging
import os

from flask import Flask, Blueprint, abort
from flask import send_from_directory
from flask_compress import Compress
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

import settings
from api.api_def import api
from api.endpoints.linebacker import linebacker_nmsp
from database.models import *

from database import db

app = Flask(__name__)
log = logging.getLogger(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_port=1, x_proto=1)


def configure_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VALIDATE
    app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    app.config["ERROR_404_HELP"] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(linebacker_nmsp)

    flask_app.register_blueprint(blueprint)

    # the toolbar is only enabled in debug mode:
    app.debug = False

    # set a 'SECRET_KEY' to enable the Flask session cookies
    app.config['SECRET_KEY'] = "<replace with a secret key>"

    Compress(app)
    # toolbar = DebugToolbarExtension(app)
    CORS(app, supports_credentials=True)

    db.init_app(flask_app)
    return app


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.png', mimetype='image/vnd.microsoft.icon')


@app.route('/ping')
def ping():
    return 'pong'


initialize_app(app)


if __name__ == "__main__":
    app.run(debug=settings.FLASK_DEBUG, host='0.0.0.0', port=5010,
            threaded=True, use_reloader=settings.RELOAD)
