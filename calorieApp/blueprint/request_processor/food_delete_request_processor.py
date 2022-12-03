from .food_modification_request_processor import FoodModificationRequestProcessor
from ...database.dao.food_entry_dao import delete_food_entry_by_id


class FoodDeleteRequestProcessor(FoodModificationRequestProcessor):

    def __init__(self):
        super(FoodDeleteRequestProcessor, self).__init__()

    def process_request(self, request):
        super(FoodDeleteRequestProcessor, self).process_request(request)
        if not self.is_request_valid:
            return
        delete_food_entry_by_id(self.targeted_food_entry)
        self.response = {'success': True, 'entry_id': self.targeted_food_entry.entry_id, 'action': 'deleted'}
        self.status = 200
