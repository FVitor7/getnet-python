class Customer:
    customer_id: str
    billing_address: dict

    def __init__(self, customer_id: str):
        if len(customer_id) > 100:
            raise TypeError("The customer_id must have bellow of 100 characters")

        self.customer_id = customer_id
        self.billing_address = {}

    def as_dict(self):
        return self.__dict__.copy()
