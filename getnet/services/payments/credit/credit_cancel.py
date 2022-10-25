from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.services.payments.payment_response import PaymentResponse


class CreditCancelResponse:
    canceled_at: datetime
    message: str

    def __init__(self, canceled_at: datetime, message: str):
        self.canceled_at = (
            canceled_at
            if isinstance(canceled_at, datetime)
            else parser.isoparse(canceled_at)
        )
        self.message = message


class CreditCancelPaymentResponse(PaymentResponse):
    credit_cancel: CreditCancelResponse

    def __init__(self, credit_cancel: Union[CreditCancelResponse, dict], **kwargs):
        super(CreditCancelPaymentResponse, self).__init__(**kwargs)
        self.credit_cancel = (
            credit_cancel
            if isinstance(credit_cancel, CreditCancelResponse) or credit_cancel is None
            else CreditCancelResponse(**credit_cancel)
        )
