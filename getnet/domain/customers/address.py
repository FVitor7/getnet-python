class Address:
    street: str
    number: str
    complement: str
    district: str
    city: str
    state: str
    country: str
    postal_code: str

    def __init__(
        self,
        street: str,
        number: str,
        complement: str,
        district: str,
        city: str,
        state: str,
        country: str,
        postal_code: str,
    ):
        self.street = street
        self.number = number
        self.complement = complement
        self.district = district
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code

    def as_dict(self):
        return self.__dict__.copy()
