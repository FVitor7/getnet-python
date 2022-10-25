import os

import pytest
from pytest_mock import MockFixture

from getnet import Client, Environment


@pytest.fixture
def client_mock(mocker: MockFixture):
    return mocker.patch("getnet.Client")


@pytest.fixture(scope="module")
def client():
    return Client(
        os.environ.get("GETNET_SELLER_ID"),
        os.environ.get("GETNET_CLIENT_ID"),
        os.environ.get("GETNET_CLIENT_SECRET"),
        Environment.HOMOLOG,
    )
