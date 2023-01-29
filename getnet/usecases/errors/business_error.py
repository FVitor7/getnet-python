from getnet.usecases.errors.request_error import RequestError


class BusinessError(RequestError):
    @property
    def details(self):
        return self.response.json().get("details")[0]

    @property
    def payment_id(self):
        return self.details.get("payment_id")

    @property
    def authorization_code(self):
        return self.details.get("authorization_code")

    @property
    def terminal_nsu(self):
        return self.details.get("terminal_nsu")

    @property
    def acquirer_transaction_id(self):
        return self.details.get("acquirer_transaction_id")

    @property
    def status(self):
        return self.details.get("status")
