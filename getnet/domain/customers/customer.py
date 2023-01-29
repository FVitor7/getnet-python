from typing import Union

from getnet.domain.customers.address import Address


class Customer:
    seller_id: str
    customer_id: str
    first_name: str
    last_name: str
    document_type: str
    document_number: str
    birth_date: str
    phone_number: str
    celphone_number: str
    email: str
    observation: str
    address: Address

    def __init__(
        self,
        first_name: str,
        last_name: str,
        document_type: str,
        document_number: str,
        birth_date: str = None,
        phone_number: str = None,
        celphone_number: str = None,
        email: str = None,
        observation: str = None,
        customer_id: str = None,
        seller_id: str = None,
        address: Union[Address, dict] = None,
    ):
        self.seller_id = seller_id
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.document_type = document_type
        self.document_number = document_number
        self.birth_date = birth_date
        self.phone_number = phone_number
        self.celphone_number = celphone_number
        self.email = email
        self.observation = observation

        if isinstance(address, dict):
            address = Address(**address)

        self.address = address

    def __str__(self):
        return "{} ({})".format(self.full_name, self.customer_id)

    def __eq__(self, other):
        return (self.seller_id, self.customer_id) == (
            other.seller_id,
            other.customer_id,
        )

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def as_dict(self):
        data = self.__dict__.copy()
        data["address"] = self.address.as_dict()
        return data
