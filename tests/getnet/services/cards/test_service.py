from getnet import Client
from getnet.services.cards import Service, Card
from getnet.services.cards.card_response import NewCardResponse
from getnet.services.service import ResponseList


def test_create(client_mock: Client, card_sample: dict):
    client_mock.post.return_value = {
        "card_id": "e8ad2ae4-9e3e-4532-998f-1a5a11e56e58",
        "number_token": "123",
    }

    service = Service(client_mock)
    card = service.create(Card(**card_sample))

    assert isinstance(card, NewCardResponse)
    assert "e8ad2ae4-9e3e-4532-998f-1a5a11e56e58" == str(card.card_id)
    assert "123" == card.number_token


def test_all(client_mock: Client, card_response_sample: dict):
    client_mock.get.return_value = {
        "cards": [card_response_sample, card_response_sample, card_response_sample]
    }

    service = Service(client_mock)
    cards = service.all("client_id")

    assert isinstance(cards, ResponseList)
    assert cards.page is None
    assert 3 == cards.total
    assert card_response_sample.get("card_id") == cards[0].card_id


def test_delete(client_mock: Client):
    client_mock.delete.return_value = True

    service = Service(client_mock)
    card = service.delete(card_id="123")

    assert card == True
    client_mock.delete.assert_called_once_with("/v1/cards/123")


def test_verify(client_mock: Client, card_sample: dict):
    client_mock.post.return_value = {"status": "VERIFIED"}

    service = Service(client_mock)
    response = service.verify(Card(**card_sample))

    assert isinstance(response, bool)
    assert True == response
