"""
Base service module
"""

import re


class Service(object):
    """
    Service Abstract an service needs
    """

    _client = None
    path: str = None

    def __init__(self, client: "Client") -> None:
        if not self.path:
            raise NotImplementedError("The classes parameter path must be defined")

        self._client = client

    def _format_url(self, path=None, **kwargs) -> str:
        data = {}

        path = self.path + path if path is not None else self.path

        match = re.search(r"{(\w+)}", path)
        if match:
            data = {}.fromkeys(list(match.groups()), "")

        data.update(**kwargs)

        return path.format(**data).rstrip("/")

    def _get(self, *args, **kwargs):
        return self._client.get(*args, **kwargs)

    def _post(self, *args, **kwargs):
        return self._client.post(*args, **kwargs)

    def _patch(self, *args, **kwargs):
        return self._client.patch(*args, **kwargs)

    def _delete(self, *args, **kwargs):
        return self._client.delete(*args, **kwargs)


class ResponseList(list):
    def __init__(self, seq=(), page=1, limit=100, total=None):
        self.page = page
        self.limit = limit
        self.total = total
        super(ResponseList, self).__init__(seq)
