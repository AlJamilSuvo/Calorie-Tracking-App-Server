from .base_request_processor import BaseRequestProcessor
from calorieApp.authentication.user_auth import authenticate_user


class AuthRequiredRequestProcessor(BaseRequestProcessor):

    def __init__(self):
        super().__init__()

    def process_request(self, request):
        super(AuthRequiredRequestProcessor, self).process_request(request)
        if not self.is_request_valid:
            return
        auth_header = request.headers.get('Authorization')
        self.requested_user = authenticate_user(auth_header)
        if self.requested_user is None:
            self.is_request_valid = False
            self.failed_response('user not authorized', 401)
