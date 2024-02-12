from typing import Union

from getnet.domain.payments.pix.pix import Pix
from getnet.domain.payments.payment_response import PaymentResponse
from getnet.application.dtos.pix import AdditionalData


class PixResponse(Pix):
    description: str
    payment_id: str
    status: str
    additional_data: dict

    def __init__(
        self,
        description: str,
        payment_id: str,
        status: str,
        additional_data: dict,
        **kwargs,
    ):
        self.description = description
        self.payment_id = payment_id
        self.status = status
        self.additional_data = additional_data

        super(PixResponse, self).__init__(**kwargs)

    def _as_dict(self):
        return self.__dict__.copy()


class PixPaymentResponse:
    description: str
    payment_id: str
    status: str
    additional_data: dict

    def __init__(
        self,
        description: str,
        payment_id: str,
        status: str,
        **kwargs,

    ):
        self.description = description
        self.payment_id = payment_id
        self.status = status
        additional_data = kwargs.get("additional_data", {})
        self.additional_data = AdditionalData(**additional_data)

    def _as_dict(self):
        return self.__dict__.copy()