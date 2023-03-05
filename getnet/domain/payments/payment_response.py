from datetime import datetime
from typing import Union
from uuid import UUID

from dateutil import parser


class PaymentResponse:
    payment_id: str
    seller_id: UUID
    amount: int
    currency: str
    order_id: str
    status: str
    received_at: str

    def __init__(
        self,
        payment_id: str,
        seller_id: Union[UUID, str],
        amount: int,
        currency: str,
        order_id: str,
        status: str,
        received_at: str = None,
    ):
        self.payment_id = payment_id
        self.seller_id = seller_id if isinstance(seller_id, UUID) else UUID(seller_id)
        self.amount = amount
        self.currency = currency
        self.order_id = order_id
        self.status = status
        self.received_at = (
            received_at
            if isinstance(received_at, datetime) or received_at is None
            else parser.isoparse(received_at)
        )

    def _as_dict(self):
        return self.__dict__.copy()