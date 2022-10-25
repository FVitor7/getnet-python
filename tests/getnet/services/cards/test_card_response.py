import pytest

from getnet.services.cards.card_response import CardResponse


def test_invalid_without_card_id(card_response_sample: dict):
    with pytest.raises(TypeError):
        card_response_sample.pop("card_id")
        CardResponse(**card_response_sample)


def testAsDict(card_response_sample: dict):
    card = CardResponse(**card_response_sample)
    value = card._as_dict()
    assert "used_at" not in value
    assert "created_at" not in value
    assert "updated_at" not in value
