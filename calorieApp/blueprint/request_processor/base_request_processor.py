def get_missing_param_list(request, param_list):
    missing_param_list = []
    for param in param_list:
        if param not in request.json:
            missing_param_list.append(param)
    return missing_param_list


class BaseRequestProcessor:

    def __init__(self):
        self.is_request_valid = None
        self.response = {}
        self.status = 500
        self.mimetype = 'application/json'
        self.is_request_valid = True
        self.requested_user = None
        self.targeted_food_entry = None

    def process_request(self, request):
        if request is None:
            self.is_request_valid = False
            self.failed_response('bad request', 400)
        else:
            self.is_request_valid = True

    def failed_response(self, reason, status):
        self.response = {'success': False, 'reason': reason}
        self.status = status

    def request_missing_parameter(self, missing_params):
        if type(missing_params) == list:
            missing_param_str = ''.join(param + ' ' for param in missing_params)
        else:
            missing_param_str = missing_params

        self.response = {'success': False, 'reason': missing_param_str + ' missing'}
        self.status = 400
