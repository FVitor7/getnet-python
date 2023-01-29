"""
Module implements the Card service responses
"""

import uuid
from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.domain.cards.card import Card
from getnet.domain.token.card_token import CardToken


class NewCardResponse(object):
    """Represents the new card registration on safe response"""

    card_id: uuid.UUID
    number_token: CardToken

    def __init__(self, card_id: str, number_token: Union[CardToken, str]):
        self.card_id = card_id if isinstance(card_id, uuid.UUID) else uuid.UUID(card_id)
        self.number_token = (
            number_token
            if isinstance(number_token, CardToken)
            else CardToken(number_token)
        )


class CardResponse(Card):
    """Represents the card (in safe) responses"""
    card_id: uuid.UUID
    last_four_digits: str
    used_at: datetime
    created_at: datetime
    updated_at: datetime
    status: str
    bin: str

    def __init__(
        self,
        card_id: Union[uuid.UUID, str],
        last_four_digits: str = None,
        used_at: str = None,
        created_at: str = None,
        updated_at: str = None,
        status: str = None,
        bin: str = None,
        **kwargs,
    ):
        self.card_id = card_id if isinstance(card_id, uuid.UUID) else uuid.UUID(card_id)
        self.last_four_digits = last_four_digits
        self.used_at = parser.isoparse(used_at) if used_at else None
        self.created_at = parser.isoparse(created_at) if created_at else None
        self.updated_at = parser.isoparse(updated_at) if updated_at else None
        self.status = status
        self.bin = bin

        kwargs.update({"cardholder_identification": None, "security_code": None})

        super(CardResponse, self).__init__(**kwargs)

    def _as_dict(self):
        data = super(CardResponse, self)._as_dict()
        data.pop("used_at")
        data.pop("created_at")
        data.pop("updated_at")
        return data
