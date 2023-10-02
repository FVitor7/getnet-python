from getnet.domain.payments.pix.pix_response import PixPaymentResponse
from getnet.domain.services import Service as BaseService

class Service(BaseService):
    path = "/v1/payments/qrcode/pix"

    def create(
        self,
        amount: int,
        currency: str,
        order_id: str,
        customer_id: str,
    ) -> PixPaymentResponse:

        data = {
            "amount": amount,
            "currency": currency,
            "order_id": order_id,
            "customer_id": customer_id,
        }

        self._client.request.headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self._client.access_token),
            "seller_id": self._client.seller_id
            }
        response = self._post(self._format_url(), json=data)
        
        return PixPaymentResponse(**response)

   