"""Implement Token Service"""

from getnet.services.service import Service as BaseService
from getnet.services.token.card_number import CardNumber
from getnet.services.token.card_token import CardToken


class Service(BaseService):
    """Represents the token service operations"""

    path = "/v1/tokens/card"

    def generate(self, card: CardNumber):
        """Generate an token for the card data

        Args:
            card (CardNumber):
        """


        self._client.request.headers = (
            {
                "Accept":"application/json, text/plain, */*",
                "Authorization": "Bearer {}".format(self._client.access_token),
                "Content-Type":"application/json"
            }
        )
        
        response = self._post(self.path, json=card.as_dict())
        return CardToken(response.get("number_token"))
