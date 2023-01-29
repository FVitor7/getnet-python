from typing import Union, Optional

from getnet.domain.payments.credit.card import Card

TRANSACTION_FULL = "FULL"
TRANSACTION_INSTALL = "INSTALL_NO_INTEREST"
TRANSACTION_INSTALL_WITH_INTEREST = "INSTALL_WITH_INTEREST"

VALID_TRANSACTION_TYPES = (
    TRANSACTION_FULL,
    TRANSACTION_INSTALL,
    TRANSACTION_INSTALL_WITH_INTEREST,
)


class Credit:
    card: Card
    delayed: bool
    authenticated: bool
    pre_authorization: bool
    save_card_data: bool
    transaction_type: str
    number_installments: int
    soft_descriptor: Optional[Union[str, None]] = None
    dynamic_mcc: Optional[Union[int, None]] = None

    def __init__(
        self,
        card: Union[Card, dict],
        transaction_type: str = TRANSACTION_FULL,
        number_installments: int = 1,
        delayed: bool = False,
        authenticated: bool = False,
        pre_authorization: bool = False,
        save_card_data: bool = False,
        soft_descriptor: str = None,
        dynamic_mcc: int = None,
    ):
        if transaction_type not in VALID_TRANSACTION_TYPES:
            raise TypeError("transaction_type is invalid")

        if soft_descriptor is not None and len(soft_descriptor) > 22:
            raise TypeError("soft_descriptor is too long (max: 23 characters)")

        self.card = card if isinstance(card, Card) or card is None else Card(**card)
        self.delayed = delayed
        self.authenticated = authenticated
        self.pre_authorization = pre_authorization
        self.save_card_data = save_card_data
        self.transaction_type = transaction_type
        self.number_installments = number_installments
        self.dynamic_mcc = dynamic_mcc
        self.soft_descriptor = soft_descriptor

    def as_dict(self):
        data = self.__dict__.copy()
        data["card"] = self.card._as_dict()

        if self.dynamic_mcc is None:
            data.pop("dynamic_mcc")

        if self.soft_descriptor is None:
            data.pop("soft_descriptor")

        return data
