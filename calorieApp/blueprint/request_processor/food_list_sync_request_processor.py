import datetime

from .auth_required_request_processor import AuthRequiredRequestProcessor
from .base_request_processor import get_missing_param_list
from ...database.dao.food_entry_dao import get_food_entry_list_after_time_for_admin, \
    get_food_entry_list_after_time_for_user
from ...database.dao.delete_food_entry_dao import get_deleted_food_entry_list_after_time_for_admin, \
    get_deleted_food_entry_list_after_time_for_user


class FoodListSyncRequest(AuthRequiredRequestProcessor):

    def __init__(self):
        super(FoodListSyncRequest, self).__init__()

    def process_request(self, request):
        super(FoodListSyncRequest, self).process_request(request)
        if not self.is_request_valid:
            return
        missing_param_list = get_missing_param_list(request, ['last_time'])
        if len(missing_param_list) > 0:
            self.request_missing_parameter(missing_param_list)
            self.is_request_valid = False
            return
        last_timestamp = request.json['last_time'] / 1000
        last_time = datetime.datetime.fromtimestamp(last_timestamp)

        if self.requested_user.is_admin:
            food_entry_list = get_food_entry_list_after_time_for_admin(last_time)
            deleted_entry_list = get_deleted_food_entry_list_after_time_for_admin(last_time)
        else:
            food_entry_list = get_food_entry_list_after_time_for_user(last_time, self.requested_user.user_id)
            deleted_entry_list = get_deleted_food_entry_list_after_time_for_user(last_time,
                                                                                 self.requested_user.user_id)

        self.response = {'success': True, 'modified': [], 'deleted': []}
        for food_entry in food_entry_list:
            self.response['modified'].append(food_entry.to_json())
            if food_entry.last_modified_time > last_time:
                last_time = food_entry.last_modified_time
        for deleted_entry in deleted_entry_list:
            self.response['deleted'].append(deleted_entry.entry_id)
            if deleted_entry.time > last_time:
                last_time = deleted_entry.time
        self.response['last_time'] = int(datetime.datetime.timestamp(last_time) * 1000)
        self.status = 200
