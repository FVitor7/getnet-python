"""Implement Token Service"""

from getnet.services.service import Service as BaseService


class Service(BaseService):
    """Represents the token service operations"""

    path = "/v1/cards/verification"

    def verification(self, card):
        """Generate an token for the card data

        Args:
            card (Card:
        """


        self._client.request.headers = (
            {
                "Accept":"application/json, text/plain, */*",
                "Authorization": "Bearer {}".format(self._client.access_token),
                "Content-Type":"application/json"
            }
        )
        
        response = self._post(self.path, json=card)
        return True if response.get("status") == "VERIFIED" else False
