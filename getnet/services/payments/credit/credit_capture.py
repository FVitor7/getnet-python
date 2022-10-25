from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.services.payments.payment_response import PaymentResponse


class CreditCaptureResponse:
    confirm_date: datetime
    message: str

    def __init__(self, confirm_date: datetime, message: str):
        self.confirm_date = (
            confirm_date
            if isinstance(confirm_date, datetime)
            else parser.isoparse(confirm_date)
        )
        self.message = message


class CreditCapturePaymentResponse(PaymentResponse):
    credit_confirm: CreditCaptureResponse

    def __init__(self, credit_confirm: Union[CreditCaptureResponse, dict], **kwargs):
        super(CreditCapturePaymentResponse, self).__init__(**kwargs)
        self.credit_confirm = (
            credit_confirm
            if isinstance(credit_confirm, CreditCaptureResponse) or credit_confirm is None
            else CreditCaptureResponse(**credit_confirm)
        )
