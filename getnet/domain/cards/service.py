"""
Implement Cards (cofre) Service
"""
import logging
import uuid
from typing import List, Union

from getnet.domain.cards.card import Card
from getnet.domain.cards.card_response import CardResponse, NewCardResponse
from getnet.domain.cards.status import Status
from getnet.domain.services import Service as BaseService, ResponseList
from getnet.domain.token.card_token import CardToken

LOGGER = logging.getLogger(__name__)


class Service(BaseService):
    """Service implements the Card service operations"""

    path = "/v1/cards/{card_id}"

    def verify(self, card: Card) -> bool:
        """Checks if the card is valid

        Args:
            card (Card): Customer card data
        """
        response = self._post(
            self._format_url(card_id="verification"), json=card._as_dict()
        )
        return response.get("status") == "VERIFIED"

    def create(self, card: Card) -> NewCardResponse:
        """Store the card in the safe

        Args:
            card (Card): Customer card data
        """
        response = self._post(self._format_url(), json=card._as_dict())
        return NewCardResponse(**response)

    def all(self, customer_id: str, status: Status = Status.ALL) -> List[CardResponse]:
        """Return an list of cards saved on safe for customer_id

        Args:
            customer_id (str): customer identify
            status: Filter of status of returned cards. Default to "all"
        """
        if status and not status in Status:
            raise AttributeError("Invalid status.")

        params = {"status": status}
        if customer_id is not None:
            params.update({"customer_id": customer_id})

        response = self._get(self._format_url(), params=params)

        cards = []
        for card in response.get("cards"):
            cards.append(CardResponse(**card))

        return ResponseList(
            cards,
            response.get("page", None),
            response.get("limit", None),
            response.get("total", len(cards)),
        )

    def get(self, card_id: Union[CardToken, uuid.UUID, str]) -> CardResponse:
        """Return the data of an saved card on the safe

        Args:
            card_id: Unique card identify on Getnet Plataform
        """
        response = self._get(self._format_url(card_id=str(card_id)))
        return CardResponse(**response)

    def delete(self, card_id: Union[CardToken, uuid.UUID, str]) -> bool:
        """Remove an card saved on safe

        Args:
            card_id: Unique card identify on Getnet Plataform
        """
        self._delete(self._format_url(card_id=str(card_id)))
        return True
