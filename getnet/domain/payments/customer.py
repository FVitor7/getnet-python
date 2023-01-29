class Customer:
    customer_id: str
    first_name: str
    last_name: str
    document_type: str
    document_number: str
    email: str

    billing_address: dict

    def __init__(self, customer: str):
        if len(customer.customer_id) > 100:
            raise TypeError("The customer_id must have bellow of 100 characters")

        self.customer_id = customer.customer_id
        self.first_name = customer.first_name
        self.last_name = customer.last_name
        self.document_type = customer.document_type
        self.document_number = customer.document_number
        self.email = customer.email
        self.billing_address = customer.address.as_dict()

    def as_dict(self):
        return self.__dict__.copy()
