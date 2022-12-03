import flask
from flask import request

from .request_processor.food_creation_request_processor import FoodEntryCreationRequestProcessor
from .request_processor.food_delete_request_processor import FoodDeleteRequestProcessor
from .request_processor.food_update_request_processor import FoodUpdateRequestProcessor
from .request_processor.food_list_fetch_request_processor import FoodListFetchRequest
from .request_processor.food_list_sync_request_processor import FoodListSyncRequest
from .base_blueprint import get_response_from_processor

food_entry_blueprint = flask.Blueprint('food_entry', __name__)
base_route = '/food_entry'


@food_entry_blueprint.route(base_route + '/add', methods=['POST'])
def api_add_food_entry():
    processor = FoodEntryCreationRequestProcessor()
    processor.process_request(request)
    return get_response_from_processor(processor)


@food_entry_blueprint.route(base_route + '/delete', methods=['POST'])
def api_delete_food_entry():
    processor = FoodDeleteRequestProcessor()
    processor.process_request(request)
    return get_response_from_processor(processor)


@food_entry_blueprint.route(base_route + '/update', methods=['POST'])
def api_update_food_entry():
    processor = FoodUpdateRequestProcessor()
    processor.process_request(request)
    return get_response_from_processor(processor)


@food_entry_blueprint.route(base_route + '/list', methods=['POST'])
def api_fetch_list_food_entry():
    processor = FoodListFetchRequest()
    processor.process_request(request)
    return get_response_from_processor(processor)


@food_entry_blueprint.route(base_route + '/sync', methods=['POST'])
def api_sync_list_food_entry():
    processor = FoodListSyncRequest()
    processor.process_request(request)
    return get_response_from_processor(processor)
