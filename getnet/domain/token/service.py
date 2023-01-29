"""Implement Token Service"""

from getnet.domain.services import Service as BaseService
from getnet.domain.token.card_number import CardNumber
from getnet.domain.token.card_token import CardToken
from getnet.infra.dtos.card_token import CardTokenResponse
from pydantic import ValidationError

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

        try:
            token_data = CardTokenResponse(**response)
        except ValidationError as e:
            raise e.errors()

        return CardToken(token_data.number_token)
