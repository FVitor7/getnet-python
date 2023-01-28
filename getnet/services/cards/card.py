"""
Implements Card Entity
"""

import re
from typing import Union, Optional

from getnet.domain.token.card_token import CardToken

BRANDS = (
    "mastercard",
    "visa",
    "amex",
    "elo",
    "hipercard",
    "Mastercard",
    "Visa",
    "Amex",
    "Elo",
    "Hipercard",
)
CARDHOLDER_IDENTIFICATION_REGEX = re.compile(r"\A\d+\Z")
VERIFY_CODE = re.compile(r"\A\d{3,4}\Z")


class Card(object):
    """Card represents the Card entity for the Cards operations"""

    customer_id: str
    number_token: CardToken
    brand: Union[str, None] = None
    cardholder_name: str
    expiration_month: str
    expiration_year: str
    cardholder_identification: Union[str, None]
    security_code: Union[str, None]
    verify_card: bool = False
    bin: Union[str, None] = None

    def __init__(
        self,
        customer_id: str,
        number_token: Union[CardToken, str],
        cardholder_name: str,
        expiration_month: int,
        expiration_year: int,
        cardholder_identification: str,
        security_code: str,
        verify_card: Optional[bool] = False,
        brand: Union[str, None] = None,
        bin: Union[str, None] = None,
    ):
        """
        Args:
            customer_id (str): Customer Identify
            number_token (CardToken|str): token of the number of card
            cardholder_name (str): Customer name as in the card
            expiration_month (int): Card expiration month
            expiration_year (int): Card expiration year (2 digits)
            cardholder_identification (str): Card owner identify (CPF, RG, etc.)
            security_code (str): Card security code (CVV or CVC)
            verify_card (bool): Optional. If true execute a transaction to check
                the card (cancel, blocked or with restriction)
            brand (str): Optional. Brand name
            bin (str): Ignore is for internal use only
        """
        if brand is not None and brand not in BRANDS:
            raise TypeError("Brand is invalid")

        if not 1 <= int(expiration_month) <= 12 or not 0 <= int(expiration_year) <= 99:
            raise TypeError("Expiration Month or Year must have 2 characters")

        if len(customer_id) > 100:
            raise TypeError("CustomerID must have bellow 100 characters.")

        if (
            cardholder_identification is not None
            and not CARDHOLDER_IDENTIFICATION_REGEX.match(cardholder_identification)
        ):
            raise TypeError("Cardholder identification invalid")

        if security_code is not None and not VERIFY_CODE.match(security_code):
            raise TypeError("Security code must have 3 or 4 characters")

        self.customer_id = customer_id
        self.number_token = (
            number_token
            if isinstance(number_token, CardToken)
            else CardToken(number_token)
        )
        self.cardholder_name = cardholder_name
        self.expiration_month = str(expiration_month)
        self.expiration_year = str(expiration_year)
        self.cardholder_identification = cardholder_identification
        self.security_code = security_code
        self.verify_card = verify_card
        self.brand = brand
        self.bin = bin

    def _as_dict(self):
        """Format the data as dict to be sent to Getnet"""
        data = self.__dict__.copy()
        data.pop("bin")
        data["number_token"] = self.number_token.number_token
        data["expiration_month"] = str(self.expiration_month).zfill(2)
        data["expiration_year"] = str(self.expiration_year).zfill(2)

        if self.security_code is None:
            data.pop("security_code")

        if self.brand is None:
            data.pop("brand")

        return data
