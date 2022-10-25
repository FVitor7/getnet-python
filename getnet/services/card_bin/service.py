"""Implement Token Service"""

from getnet.services.service import Service as BaseService
from getnet.services.verification.card_verification import CardVerification
from getnet.services.verification.card_verified import CardVerified


class Service(BaseService):
    """Represents the token service operations"""

    path = "/v1/cards/binlookup/"

    def binlookup(self, card_bin: str):
        self._client.request.headers = (
            {
                "Authorization": "Bearer {}".format(self._client.access_token),
            }
        )

        url = f"{self.path}{card_bin}"

        response = self._get(url)

        return response.json()
