from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.domain.payments.payment_response import PaymentResponse


class CreditAdjustPaymentResponse(PaymentResponse):
    authorization_code: str
    authorized_at: datetime
    reason_code: int
    reason_message: str
    acquirer: str
    soft_descriptor: str
    terminal_nsu: str
    acquirer_transaction_id: str
    adjustment_acquirer_transaction_id: str
    
    def __init__(
        self,
        authorization_code: str,
        authorized_at: Union[datetime, str],
        reason_code: int,
        reason_message: str,
        acquirer: str,
        soft_descriptor: str,
        terminal_nsu: str,
        acquirer_transaction_id: str,
        adjustment_acquirer_transaction_id: str,
        **kwargs,
    ):
        self.authorization_code = authorization_code
        self.authorized_at = (
            authorized_at
            if isinstance(authorized_at, datetime)
            else parser.isoparse(authorized_at)
        )
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.acquirer = acquirer
        self.acquirer_transaction_id = acquirer_transaction_id
        self.terminal_nsu = terminal_nsu
        self.soft_descriptor = soft_descriptor
        self.adjustment_acquirer_transaction_id = adjustment_acquirer_transaction_id

        super(CreditAdjustPaymentResponse, self).__init__(**kwargs)

    def as_dict(self) -> dict:
        """Format the data as dict to be sent to Getnet"""
        return self.__dict__.copy()