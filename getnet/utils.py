from requests.models import Response

from getnet.usecases import errors


class handler_request:
    def __init__(self, client, logger):
        """
        Args:
            client:
        """
        self.client = client
        self.logger = logger

    def __enter__(self):
        if self.client.access_token_expired():
            self.client.auth()

        return self.logger

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Args:
            exc_type:
            exc_val:
            exc_tb:
        """
        pass


def handler_request_exception(response: Response):
    """
    Args:
        response (Response):
    """
    status_code = response.status_code
    data = response.json()
    if "details" in data and len(data.get("details")) > 0:
        data = data.get("details")[0]

    kwargs = {
        "error_code": data.get("error_code")
        or data.get("error")
        or str(data.get("status_code")),
        "description": data.get("description_detail")
        or data.get("description")
        or data.get("error_description")
        or data.get("message"),
        "response": response,
    }

    message = "{} {} ({})".format(
        kwargs.get("error_code"),
        kwargs.get("description"),
        response.url,
    )

    if status_code == 400:
        return errors.BadRequest(message, **kwargs)
    elif status_code == 402:
        return errors.BusinessError(message, **kwargs)
    elif status_code == 404:
        return errors.NotFound(message, **kwargs)
    elif status_code == 500:
        return errors.ServerError(message, **kwargs)
    elif status_code == 503:
        return errors.ServiceUnavailable(message, **kwargs)
    elif status_code == 504:
        return errors.GatewayTimeout(message, **kwargs)
    else:
        return errors.RequestError(message, **kwargs)
