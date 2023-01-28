from getnet.usecases.errors.request_error import RequestError

__ALL__ = [
    "BadRequest",
    "NotFound",
    "ServerError",
    "ServiceUnavailable",
    "GatewayTimeout",
]


class BadRequest(RequestError):
    pass


class NotFound(RequestError):
    pass


class ServerError(RequestError):
    pass


class ServiceUnavailable(RequestError):
    pass


class GatewayTimeout(RequestError):
    pass
