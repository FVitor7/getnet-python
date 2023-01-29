"""Implements the CardNumber entity"""
import re


class CardVerification:
    """Implements the CardNumber data required to generate the tokenized
    version
    """

    number_token: str
    brand: str
    cardholder_name: str
    expiration_month: str
    expiration_year: str
    security_code: str


    def __init__(self, number_token: str, expiration_month: str, expiration_year: str, cardholder_name: str, brand: str = None, security_code: str = None):
        """
        Args:
            card_number (str): An valid card number
            customer_id (str): Customer identify
        """
        if not number_token:
            raise AttributeError(
                "Card Token is invalid or empty!"
            )

        self.number_token = number_token
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        
        if brand:
            self.brand = brand
        if cardholder_name:
            self.cardholder_name = cardholder_name
        if security_code:
            self.security_code = security_code


    def as_dict(self) -> dict:
        """Format the data as dict to be sent to Getnet"""
        return self.__dict__.copy()
