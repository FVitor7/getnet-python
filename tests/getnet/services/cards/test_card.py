import pytest

from getnet.services.cards.card import Card
from getnet.services.token.card_token import CardToken


def test_invalid_expiration_month(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["expiration_month"] = 13
        Card(**card_sample)


def test_invalid_expiration_year(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["expiration_year"] = 100
        Card(**card_sample)


def test_invalid_customer_id(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["customer_id"] = "1" * 101
        Card(**card_sample)


def test_invalid_security_code2(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["security_code"] = "12"
        Card(**card_sample)


def test_invalid_security_code5(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["security_code"] = "12345"
        Card(**card_sample)


def test_number_token_as_str(card_sample: dict):
    card_sample["number_token"] = "12345"
    card = Card(**card_sample)

    assert isinstance(card.number_token, CardToken)
    assert "12345" == card.number_token.number_token


def test_invalid_brand(card_sample: dict):
    with pytest.raises(TypeError):
        card_sample["brand"] = "12345"
        Card(**card_sample)


def test_as_dict(card_sample: dict):
    card = Card(**card_sample)
    assert card_sample == card._as_dict()
