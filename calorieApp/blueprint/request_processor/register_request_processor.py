from .base_request_processor import BaseRequestProcessor
from ...database.dao.user_dao import create_user, get_user_by_user_id
from ...authentication.user_auth import get_user_auth_token


class RegisterRequestProcessor(BaseRequestProcessor):

    def __init__(self):
        super().__init__()

    def process_request(self, request):
        super(RegisterRequestProcessor, self).process_request(request)
        if 'user_id' not in request.json:
            self.is_request_valid = False
            self.request_missing_parameter('user_id')
            return
        user_id = request.json['user_id']
        user = get_user_by_user_id(user_id=user_id)
        if user is None:
            user = create_user(user_id)
        auth_token = get_user_auth_token(user)
        self.response = {'user_id': user.user_id, 'is_admin': user.is_admin, 'token': auth_token, 'success': True}
        self.status = 200
