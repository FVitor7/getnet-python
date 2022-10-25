import pytest

from getnet.services.token import Service, CardNumber
from getnet.services.token.card_token import CardToken


@pytest.mark.vcr()
def test_generate(client):
    service = Service(client)
    number_token = service.generate(CardNumber("5155901222280001", "customer_21081826"))

    assert isinstance(number_token, CardToken)
    assert number_token.number_token is not None
