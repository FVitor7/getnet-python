import pytest

from getnet.errors import BadRequest, NotFound
from getnet.services.cards import Service, Card
from getnet.services.cards.card_response import NewCardResponse
from getnet.services.service import ResponseList


@pytest.mark.vcr
def test_create(client, card_sample: dict):
    card_sample["number_token"] = client.generate_card_token(
        "5155901222280001", "getnet-py"
    )
    card = Service(client).create(Card(**card_sample))

    assert isinstance(card, NewCardResponse)
    assert card_sample["number_token"] == card.number_token.number_token


@pytest.mark.vcr
def test_invalid_create(client, card_sample: dict):
    with pytest.raises(BadRequest) as excinfo:
        card_sample["number_token"] = "123"
        Service(client).create(Card(**card_sample))

    assert "TOKENIZATION-400" == excinfo.value.error_code


@pytest.mark.vcr
def test_get(client, card_sample: dict):
    card_sample["number_token"] = client.generate_card_token(
        "5155901222280001", "getnet-py"
    )
    service = Service(client)
    sample_card = service.create(Card(**card_sample))

    card = service.get(sample_card.card_id)

    assert isinstance(card, Card)
    assert sample_card.card_id == card.card_id


@pytest.mark.vcr
def test_invalid_get(client):
    with pytest.raises(NotFound) as excinfo:
        Service(client).get("14a2ce5d-ebc3-49dc-a516-cb5239b02285")

    assert "404" == excinfo.value.error_code


@pytest.mark.vcr
def test_all(client, card_sample: dict):
    cards = Service(client).all(card_sample.get("customer_id"))
    assert isinstance(cards, ResponseList)
    assert cards.page is None
    assert cards.limit is None
    assert cards.total is not None


@pytest.mark.vcr
def test_all_not_found(client):
    with pytest.raises(NotFound) as excinfo:
        Service(client).all("foobar")

    assert "404" == excinfo.value.error_code


@pytest.mark.vcr
def test_delete(client, card_sample: dict):
    card_sample["number_token"] = client.generate_card_token(
        "5155901222280001", "getnet-py"
    )
    service = Service(client)

    created_card = service.create(Card(**card_sample))
    card = service.get(created_card.card_id)

    resp = service.delete(card.card_id)
    assert True == resp


@pytest.mark.vcr
def test_delete_not_found(client):
    with pytest.raises(NotFound) as excinfo:
        cards = Service(client).delete("72402c54-6bd3-4895-a6b4-adfded0c11dc")

    assert "VAULT-404" == excinfo.value.error_code
