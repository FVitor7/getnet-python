from requests.exceptions import RequestException


class RequestError(RequestException):
    def __init__(self, *args, **kwargs):
        self.error_code = kwargs.pop("error_code")
        self.description = kwargs.pop("description")
        super(RequestError, self).__init__(*args, **kwargs)
