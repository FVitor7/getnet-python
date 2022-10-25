"""Implements the Card Token entity"""


class CardVerified:
    """Represent the card number tokenized version"""

    status: bool

    def __init__(self, status: str):
        """
        Args:
            number_token (str):
        """
        self.status = True if status == "VERIFIED" else False
