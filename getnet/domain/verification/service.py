"""Implement Token Service"""

from getnet.domain.services import Service as BaseService
from getnet.domain.verification.card_verification import CardVerification
from getnet.domain.verification.card_verified import CardVerified
from getnet.infra.dtos.card_verification import CardVerificationResponse
from pydantic import ValidationError


class CardVerificationService(BaseService):
    """Represents the token service operations"""

    path = "/v1/cards/verification"

    def verification(self, card: CardVerification):
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
        
        response = self._post(self.path, json=card.as_dict())
        
        try:
            card_verification_data = CardVerificationResponse(**response)
        except ValidationError as e:
            raise e.errors()

        return CardVerified(card_verification_data.status)
