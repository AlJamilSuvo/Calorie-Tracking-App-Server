import datetime

from .auth_required_request_processor import AuthRequiredRequestProcessor
from .base_request_processor import get_missing_param_list
from ...database.dao.food_entry_dao import get_food_entry_list_for_user, get_food_entry_list_for_all_user


class FoodListFetchRequest(AuthRequiredRequestProcessor):

    def __init__(self):
        super(FoodListFetchRequest, self).__init__()

    def process_request(self, request):
        super(FoodListFetchRequest, self).process_request(request)
        if not self.is_request_valid:
            return
        missing_param_list = get_missing_param_list(request, ['from_time', 'to_time'])
        if len(missing_param_list) > 0:
            self.request_missing_parameter(missing_param_list)
            self.is_request_valid = False
            return
        from_timestamp = request.json['from_timestamp'] / 1000
        to_timestamp = request.json['to_timestamp'] / 1000

        from_time = datetime.datetime.fromtimestamp(from_timestamp)
        to_time = datetime.datetime.fromtimestamp(to_timestamp)

        if self.requested_user.is_admin:
            food_entry_list = get_food_entry_list_for_all_user(from_time, to_time)
        else:
            food_entry_list = get_food_entry_list_for_user(self.requested_user.user_id, from_time, to_time)

        self.response = {'success': True, 'list': []}
        for food_entry in food_entry_list:
            self.response['list'].append(food_entry.to_json())
        self.status = 200
