from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.domain.payments.payment_response import PaymentResponse


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

    def _as_dict(self):
        return self.__dict__.copy()

class CreditCapturePaymentResponse(PaymentResponse):
    credit_confirm: CreditCaptureResponse

    def __init__(self, credit_confirm: Union[CreditCaptureResponse, dict], **kwargs):
        super(CreditCapturePaymentResponse, self).__init__(**kwargs)
        self.credit_confirm = (
            credit_confirm
            if isinstance(credit_confirm, CreditCaptureResponse) or credit_confirm is None
            else CreditCaptureResponse(**credit_confirm)
        )
    
    def as_dict(self) -> dict:
        """Format the data as dict to be sent to Getnet"""
        data = self.__dict__.copy()
        data["credit_confirm"] = self.credit_confirm._as_dict()

        return data
