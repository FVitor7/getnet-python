from datetime import timedelta, datetime

import pytest
from pytest_mock import MockerFixture

from getnet import Client
from getnet.usecases.errors import RequestError
from getnet.services import cards, customers
from getnet.domain.token.card_token import CardToken
from getnet.domain import token
import os

seller_id = os.getenv('SELLER_ID')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

@pytest.fixture
def client():
    return Client(
        seller_id,
        client_id,
        client_secret,
    )


class TestClientAuth:
    def test_invalid_data(self, client, mocker: MockerFixture) -> None:
        session_get_mock = mocker.patch(
            "requests.Session.get", return_value=mocker.MagicMock()
        )
        session_get_mock.ok.return_value = False

        with pytest.raises(RequestError):
            client.auth()

    def test_missing_access_token(self, client, mocker: MockerFixture) -> None:
        mocker.patch("getnet.Client.auth", return_value=True)
        session_get_mock = mocker.patch(
            "requests.Session.get", return_value=mocker.MagicMock()
        )
        session_get_mock.ok.return_value = True

        access_token_expired = mocker.spy(client, "access_token_expired")
        client.access_token = None

        client.get("/test")
        access_token_expired.assert_called_once()
        client.auth.assert_called_once()

    def test_expired_access_token(self, client, mocker: MockerFixture) -> None:
        mocker.patch("getnet.Client.auth", return_value=True)
        session_get_mock = mocker.patch(
            "requests.Session.get", return_value=mocker.MagicMock()
        )
        session_get_mock.ok.return_value = True

        access_token_expired = mocker.spy(client, "access_token_expired")
        client.access_token = "test"
        client.access_token_expires = int(
            datetime.timestamp(datetime.now() + timedelta(seconds=-3600))
        )

        client.get("/test")
        access_token_expired.assert_called_once()
        client.auth.assert_called_once()


def test_token_service(client, mocker: MockerFixture) -> None:
    mocker.patch("getnet.Client.auth", return_value=True)

    assert isinstance(client.token_service(), token.Service)


def test_generate_token_card_shortcut(client, mocker: MockerFixture):
    mocker.patch("getnet.Client.auth", return_value=True)
    token_service_mock = mocker.patch.object(token.Service, "generate")
    token_service_mock.return_value = CardToken("123")

    response = client.generate_card_token("5155901222280001", "customer_21081826")

    assert response.number_token == "123"
    token_service_mock.assert_called_once()
