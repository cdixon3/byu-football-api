import logging
import traceback

from flask import request
from flask_restplus import Api
import settings
from sqlalchemy.orm.exc import NoResultFound
from functools import wraps

log = logging.getLogger(__name__)

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = request.headers['X-API-KEY'] if 'X-API-KEY' in request.headers else None

        if not token:
            # This does not need jsonified as it's used within
            return {'message': 'Token is missing.'}, 401

        if token != 'myToken':
            return {'message': 'Invalid Token.'}, 401

        print("TOKEN: {}".format(token))

        return f(*args, **kwargs)

    return decorated


api = Api(version='1.0', title='BYU Football API',
          description='Supply data to create audience workshop content.')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
