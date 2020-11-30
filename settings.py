import os
from api.api_def import api

linebacker_nmsp = api.namespace('byu_football_api', path='/linebacker',
                                description='Operations related to linebackers')

DB_BASE_PATH: str = "postgres"

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION: str = 'list'
RESTPLUS_VALIDATE: bool = True
RESTPLUS_MASK_SWAGGER: bool = False
RESTPLUS_ERROR_404_HELP: bool = False

SQLALCHEMY_DATABASE_URI: str = f"postgresql:///{DB_BASE_PATH}"
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

# Flask settings
FLASK_DEBUG: bool = os.environ.get("FLASK_DEBUG") == "True"

# SET ENVIRONMENT VARIABLES
RELOAD: bool = os.environ.get('RELOAD', True)
