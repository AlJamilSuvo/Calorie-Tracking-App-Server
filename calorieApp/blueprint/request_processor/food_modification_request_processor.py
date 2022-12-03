from .auth_required_request_processor import AuthRequiredRequestProcessor
from ...database.dao.food_entry_dao import get_food_entry_by_id


class FoodModificationRequestProcessor(AuthRequiredRequestProcessor):

    def __init__(self):
        super().__init__()

    def process_request(self, request):
        super(FoodModificationRequestProcessor, self).process_request(request)
        if not self.is_request_valid:
            return

        if 'entry_id' not in request.json:
            self.request_missing_parameter('entry_id')
            self.is_request_valid = False
            return

        entry_id = request.json['entry_id']
        self.targeted_food_entry = get_food_entry_by_id(entry_id)
        if self.targeted_food_entry is None:
            self.is_request_valid = False
            self.failed_response('food entry not found', 400)
            return

        if not self.requested_user.is_admin:
            if self.targeted_food_entry.user_id != self.requested_user.user_id:
                self.is_request_valid = False
                self.failed_response('not allowed to modify this food entry', 400)
                return
