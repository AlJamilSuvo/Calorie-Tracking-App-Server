import datetime

from .auth_required_request_processor import AuthRequiredRequestProcessor
from .base_request_processor import get_missing_param_list
from ...database.dao.food_entry_dao import create_food_entry
from ...database.dao.user_dao import get_user_by_user_id


class FoodEntryCreationRequestProcessor(AuthRequiredRequestProcessor):

    def __init__(self):
        super(FoodEntryCreationRequestProcessor, self).__init__()

    def process_request(self, request):
        super(FoodEntryCreationRequestProcessor, self).process_request(request)
        if not self.is_request_valid:
            return
        missing_param_list = get_missing_param_list(request, ['food_name', 'calorie', 'timestamp'])
        if len(missing_param_list) > 0:
            self.request_missing_parameter(missing_param_list)
            self.is_request_valid = False
            return
        user = None
        if self.requested_user.is_admin:
            if 'user_id' not in request.json:
                self.request_missing_parameter(missing_param_list)
                self.is_request_valid = False
                return

            user_id = request.json['user_id']
            user = get_user_by_user_id(user_id)
            if user is None:
                self.failed_response('user does not exists', 400)
                self.is_request_valid = False
                return
        else:
            if 'user_id' in request.json:
                user_id = request.json['user_id']
                if user_id != self.requested_user.user_id:
                    self.failed_response('not allowed to create food entry', 400)
                    self.is_request_valid = False
                    return
            user = self.requested_user
        food_name = request.json['food_name']
        calorie = request.json['calorie']
        timestamp = request.json['timestamp'] / 1000
        time = datetime.datetime.fromtimestamp(timestamp)

        self.targeted_food_entry = create_food_entry(user, food_name, calorie, time)
        self.response = self.targeted_food_entry.to_json()
        self.response['success'] = True
        self.status = 200
