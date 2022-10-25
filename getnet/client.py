import logging
from datetime import datetime, timedelta
from typing import Union, Optional

import requests

from getnet.environment import Environment
from getnet.services import card_bin, token, verification, payments
from getnet.services.payments.credit import card
from getnet.services.token.card_token import CardToken
from getnet.utils import handler_request, handler_request_exception

__all__ = ["Client"]

LOGGER = logging.getLogger(__name__)


class Client(object):
    """Return an SDK client"""

    request: requests.Session
    seller_id: Optional[Union[str, None]] = None
    client_id: Optional[Union[str, None]] = None
    client_secret: Optional[Union[str, None]] = None
    environment: Environment = Environment.SANDBOX
    access_token: Optional[Union[str, None]] = None
    access_token_expires: Optional[Union[int, None]] = None

    def __init__(
        self,
        seller_id: str,
        client_id: str,
        client_secret: str,
        environment: Environment = Environment.SANDBOX,
    ):
        """
        Args:
            seller_id (str):
            client_id (str):
            client_secret (str):
            environment (Environment):
        """
        self.seller_id = seller_id
        self.client_id = client_id
        self.client_secret = client_secret

        if not isinstance(environment, Environment):
            raise AttributeError("Invalid environment")

        self.environment = environment
        self.base_url = environment.base_url()

        self._setup_client()

    def _setup_client(self) -> None:
        self.request = requests.Session()
        self.request.headers.update(
            {"user-agent": "getnet-py/1.1", "seller_id": self.seller_id}
        )

    def _handler_request(self):
        return handler_request(self, LOGGER)

    def access_token_expired(self) -> bool:
        """Returns true if not have an token or is expired

        Returns:
            bool
        """
        return (
            self.access_token is None
            or self.access_token_expires < datetime.timestamp(datetime.now())
        )

    def auth(self) -> None:
        if self.access_token_expired():
            path = "/auth/oauth/v2/token"
            data = {"scope": "oob", "grant_type": "client_credentials"}

            response = self.request.post(
                self.base_url + path,
                data=data,
                auth=(self.client_id, self.client_secret),
            )
            if not response.ok:
                raise handler_request_exception(response)

            response_data = response.json()

            self.access_token = response_data.get("access_token")
            self.access_token_expires = int(
                datetime.timestamp(
                    datetime.now() + timedelta(seconds=response_data.get("expires_in"))
                )
            )
            self.request.headers.update(
                {"Authorization": "Bearer {}".format(self.access_token)}
            )

    def get(self, path, **kwargs) -> dict:
        """
        Args:
            path:
            **kwargs:
        """
        with handler_request(self, LOGGER):
            url = self.base_url + path
            response = self.request.get(url, **kwargs)
            if not response.ok:
                raise handler_request_exception(response)
            return response.json()

    def post(self, path: str, **kwargs) -> dict:
        """
        Args:
            path (str):
            **kwargs:
        """
        with handler_request(self, LOGGER):
            url = self.base_url + path
            response = self.request.post(url, **kwargs)
            if not response.ok:
                raise handler_request_exception(response)
            return response.json()

    def patch(self, path: str, **kwargs) -> dict:
        """
        Args:
            path (str):
            **kwargs:
        """
        with handler_request(self, LOGGER):
            url = self.base_url + path
            response = self.request.patch(url, **kwargs)
            if not response.ok:
                raise handler_request_exception(response)
            return response.json()

    def delete(self, path: str, **kwargs) -> Union[bool, dict]:
        """
        Args:
            path (str):
            **kwargs:
        """
        with handler_request(self, LOGGER):
            url = self.base_url + path
            response = self.request.delete(url, **kwargs)
            if not response.ok:
                raise handler_request_exception(response)

            return True

    def token_service(self) -> token.Service:
        """Return a instance of token service"""
        return token.Service(self)

    def generate_card_token(self, card_number: str, customer_id: str) -> CardToken:
        """Shortcut to card token generation

        Args:
            card_number (str): credit card number
            customer_id (str): Customer identify

        Raises:
            * AttributeError, RequestError
        """
        return self.token_service().generate(token.CardNumber(card_number, customer_id))

    def verification_service(self) -> verification.Service:
        """Return a instance of token service"""
        return verification.Service(self)

    def card_verified(self, number_token, expiration_month, expiration_year,  cardholder_name, brand=None, security_code=None) -> bool:
        return self.verification_service().verification(verification.CardVerification(number_token, expiration_month, expiration_year, cardholder_name, brand, security_code))

    def check_bin_service(self) -> card_bin.Service:
        """Return a instance of token service"""
        return card_bin.Service(self)

    def card_bin(self, card_bin: str) -> dict:
        return self.check_bin_service().binlookup(card_bin)

    def order(self, order_id: str, sales_tax: int = None, product_type: str = None) -> payments.Order:
        return payments.Order(order_id, sales_tax, product_type)
    
    def customer(self, customer_id: str) -> payments.Customer:
        return payments.Customer(customer_id)
    
    # Payments  Credit
    def payment_credit_service(self) -> payments.credit.Service:
        """Return a instance of token service"""
        return payments.credit.Service(self)

    def credit_card(self,number_token, cardholder_name, security_code, brand, expiration_month, expiration_year) -> card.Card:
        return card.Card(number_token=number_token, cardholder_name=cardholder_name, security_code=security_code, brand=brand, expiration_month=expiration_month, expiration_year=expiration_year)

    def create_credit_transaction(self, amount, delayed, pre_authorization, save_card_data, transaction_type, number_installments, order, customer, card, currency="BRL") -> payments.credit.Service:
        credit = {
            "delayed": delayed,
            "pre_authorization": pre_authorization,
            "save_card_data": save_card_data,
            "transaction_type": transaction_type,
            "number_installments": number_installments,
            "card": card._as_dict()
        }

        return self.payment_credit_service().create(amount, currency, order, credit, customer)

    def cancel_credit_transaction(self, payment_id):
        return self.payment_credit_service().cancel(payment_id)

    def capture_credit_transaction(self, payment_id: str, amount: str):
        return self.payment_credit_service().capture(payment_id, amount)

    def adjust_credit_transaction(self, payment_id: str, amount: str, currency="BRL"):
        return self.payment_credit_service().adjust(payment_id, amount, currency)