import unittest

import pytest

from getnet.services.token import CardNumber


def test_invalid_card_number():
    with pytest.raises(AttributeError):
        CardNumber("123", "123")


def test_invalid_customer_id():
    with pytest.raises(AttributeError):
        CardNumber("5155901222280001", "a" * 101)


def test_get_as_dict():
    object = CardNumber("5155901222280001", "customer_21081826")
    assert {
        "card_number": "5155901222280001",
        "customer_id": "customer_21081826",
    } == object.as_dict()
