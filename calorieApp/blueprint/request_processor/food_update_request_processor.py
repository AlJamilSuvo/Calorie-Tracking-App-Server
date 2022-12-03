import datetime

from .food_modification_request_processor import FoodModificationRequestProcessor
from .base_request_processor import get_missing_param_list
from ...database.dao.food_entry_dao import update_food_entry


class FoodUpdateRequestProcessor(FoodModificationRequestProcessor):

    def __init__(self):

        super().__init__()

    def process_request(self, request):
        super(FoodUpdateRequestProcessor, self).process_request(request)
        if not self.is_request_valid:
            return
        missing_param_list = get_missing_param_list(request, ['food_name', 'calorie', 'timestamp'])
        if len(missing_param_list) > 0:
            self.request_missing_parameter(missing_param_list)
            self.is_request_valid = False
            return

        food_name = request.json['food_name']
        calorie = request.json['calorie']
        timestamp = request.json['timestamp'] / 1000
        time = datetime.datetime.fromtimestamp(timestamp)
        self.targeted_food_entry.food_name = food_name
        self.targeted_food_entry.calorie = calorie
        self.targeted_food_entry.time = time
        update_food_entry(self.targeted_food_entry)
        self.response = self.targeted_food_entry.to_json()
        self.response['success'] = True
        self.status = 200
