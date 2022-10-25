from typing import Union
from uuid import UUID

from getnet.services.payments import Customer
from getnet.services.payments.credit.credit import Credit
from getnet.services.payments.credit.credit_adjust import CreditAdjustPaymentResponse
from getnet.services.payments.credit.credit_cancel import CreditCancelPaymentResponse
from getnet.services.payments.credit.credit_capture import CreditCapturePaymentResponse
from getnet.services.payments.credit.credit_response import CreditPaymentResponse
from getnet.services.payments.order import Order
from getnet.services.service import Service
from getnet.services.utils import Device


class Service(Service):
    path = "/v1/payments/credit"

    def create(
        self,
        amount: int,
        currency: str,
        order: Order,
        credit: Credit,
        customer: Customer,
        device: Device = None,
    ) -> CreditPaymentResponse:
        
        data = {
            "seller_id": self._client.seller_id,
            "amount": amount,
            "currency": currency,
            "order": order.as_dict(),
            "credit": credit, #.as_dict(),
            "customer": customer.as_dict(),
            "device": {},
            "shippings": [{
                "address": {

                }
            }],
            "sub_merchant": {}
        }

        if device is not None:
            data["device"] = device.as_dict()

        self._client.request.headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self._client.access_token),
            "seller_id": self._client.seller_id
            }

        response = self._post(self._format_url(), json=data)
        
        return CreditPaymentResponse(**response)

    def cancel(self, payment_id: Union[UUID, str]) -> CreditCancelPaymentResponse:
        response = self._post(
            self._format_url(path="/{payment_id}/cancel", payment_id=str(payment_id))
        )
        return CreditCancelPaymentResponse(**response)

    def capture(
        self,
        payment_id: Union[UUID, str], amount
    ) -> CreditCapturePaymentResponse:
      
        self._client.request.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {}".format(self._client.access_token),
            }

        data = {
            "amount":amount
        }

        response = self._post(self._format_url(path="/{payment_id}/confirm", payment_id=str(payment_id)), json=data)

        return CreditCapturePaymentResponse(**response)


    def adjust(
        self,
        payment_id: Union[UUID, str], amount: str, currency="BRL"
    ) -> CreditAdjustPaymentResponse:
      
        self._client.request.headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {}".format(self._client.access_token),
            }

        data = {
            "amount":amount,
            "currency": currency,
        }

        response = self._post(self._format_url(path="/{payment_id}/adjustment", payment_id=str(payment_id)), json=data)
        return CreditAdjustPaymentResponse(**response)