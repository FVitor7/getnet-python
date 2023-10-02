from typing import Union, Optional


class Pix:
    amount: int
    currency: str
    order_id: str
    customer_id: str
    

    def __init__(
        self,
        amount: int,
        currency: str,
        order_id: str,
        customer_id: str,
    ):
        self.amount = amount
        self.currency = currency
        self.order_id = order_id
        self.customer_id = customer_id

    def as_dict(self):
        data = self.__dict__.copy()
        return data
