import logging
from datetime import datetime, timedelta
from typing import Union, Optional

import requests
from getnet.domain.authentication import Authentication

from getnet.usecases.environment import Environment
from getnet.domain import payments
from getnet.domain.card_bin import CardBinInfo
from getnet.domain.verification import CardVerificationService, CardVerification
from getnet.domain.token import Service as TokenService
from getnet.domain.customers import Service as CustomersService
from getnet.domain.payments.credit import card
from getnet.domain.token.card_token import CardToken
from getnet.domain.token.card_number import CardNumber
from getnet.domain.customers import Customer, Address
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

        if not self.access_token:
            self.auth()

    def _setup_client(self) -> None:
        self.request = requests.Session()
        self.request.headers.update(
            {"user-agent": "getnet-py/1.1", "seller_id": self.seller_id}
        )

    def _handler_request(self):
        return handler_request(self, LOGGER)

    def access_token_expired(self) -> Authentication.access_token_expired:
        return Authentication.access_token_expired(self)
    
    def auth(self) -> Authentication.auth:
        return Authentication.auth(self)

    
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

    def generate_card_token(self, card_number: str, customer_id: str) -> CardToken:
        """Shortcut to card token generation

        Args:
            card_number (str): credit card number
            customer_id (str): Customer identify

        Raises:
            * AttributeError, RequestError
        """
        return TokenService(self).generate(CardNumber(card_number, customer_id))


    def card_verified(self, number_token, expiration_month, expiration_year,  cardholder_name, brand=None, security_code=None) -> bool:
        return CardVerificationService(self).verification(CardVerification(number_token, expiration_month, expiration_year, cardholder_name, brand, security_code))

    def card_bin(self, card_bin: str) -> dict:
        return CardBinInfo(self).binlookup(card_bin)

    def order(self, order_id: str, sales_tax: int = None, product_type: str = None) -> payments.Order:
        return payments.Order(order_id, sales_tax, product_type)
    
    def customer_service(self) -> CustomersService:
        """Return a instance of token service"""
        return CustomersService(self)

    def customer(self, customer_data) -> Customer:
        return Customer(**customer_data)

    def payment_customer(self, customer) -> payments.Customer:
        return payments.Customer(customer)
    
    def payment_credit_service(self) -> payments.credit.Service:
        """Return a instance of token service"""
        return payments.credit.Service(self)

    def credit_card(self,number_token, cardholder_name, security_code, brand, expiration_month, expiration_year) -> card.Card:
        return card.Card(number_token=number_token, cardholder_name=cardholder_name, security_code=security_code, brand=brand, expiration_month=expiration_month, expiration_year=expiration_year)

    def create_credit_transaction(self, amount, delayed, pre_authorization, save_card_data, transaction_type, number_installments, order, customer, card, shipping_address, currency="BRL") -> payments.credit.Service:
        credit = {
            "delayed": delayed,
            "pre_authorization": pre_authorization,
            "save_card_data": save_card_data,
            "transaction_type": transaction_type,
            "number_installments": number_installments,
            "card": card._as_dict(),
        }

        return self.payment_credit_service().create(amount, currency, order, credit, customer, shipping_address)

    def cancel_credit_transaction(self, payment_id):
        return self.payment_credit_service().cancel(payment_id)

    def capture_credit_transaction(self, payment_id: str, amount: str):
        return self.payment_credit_service().capture(payment_id, amount)

    def adjust_credit_transaction(self, payment_id: str, amount: str, currency="BRL"):
        return self.payment_credit_service().adjust(payment_id, amount, currency)