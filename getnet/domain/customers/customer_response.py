from getnet.domain.customers.customer import Customer


class CustomerResponse(Customer):
    status: str

    def __init__(self, status: str, **kwargs):
        self.status = status
        super(CustomerResponse, self).__init__(**kwargs)
