"""Implements the Card Token entity"""


class CardToken:
    """Represent the card number tokenized version"""

    number_token: str

    def __init__(self, number_token: str):
        """
        Args:
            number_token (str):
        """
        self.number_token = number_token

    def __str__(self):
        return str(self.number_token)

    def __eq__(self, other):
        match = other.number_token if isinstance(other, CardToken) else other
        return self.number_token == match
