import flask

from .request_processor.register_request_processor import RegisterRequestProcessor
from .base_blueprint import get_response_from_processor

user_blueprint = flask.Blueprint('user', __name__)
base_route = '/user'


@user_blueprint.route(base_route + '/register', methods=['POST'])
def api_register_user():
    processor = RegisterRequestProcessor()
    processor.process_request(flask.request)
    return get_response_from_processor(processor)
