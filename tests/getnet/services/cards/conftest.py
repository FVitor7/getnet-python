import uuid

import pytest

from getnet.services.token.card_token import CardToken


@pytest.fixture
def card_sample():
    return {
        "number_token": CardToken("123"),
        "brand": "visa",
        "cardholder_name": "John Doe",
        "cardholder_identification": "5155901222280001",
        "security_code": "123",
        "expiration_month": "02",
        "expiration_year": "25",
        "customer_id": "johndoe",
        "verify_card": False,
    }.copy()


@pytest.fixture
def card_response_sample():
    return {
        "card_id": uuid.UUID("e8ad2ae4-9e3e-4532-998f-1a5a11e56e58"),
        "number_token": CardToken("123"),
        "brand": "visa",
        "cardholder_name": "John Doe",
        "cardholder_identification": "5155901222280001",
        "security_code": "123",
        "expiration_month": "02",
        "expiration_year": "25",
        "customer_id": "johndoe",
        "verify_card": True,
        "last_four_digits": "1212",
        "used_at": "2017-04-19T16:30:30.003Z",
        "created_at": "2017-04-19T16:30:30.003Z",
        "updated_at": "2017-04-19T16:30:30.003Z",
        "status": "active",
        "bin": "123",
    }.copy()
