import pytest

from getnet import Client
from getnet.errors import BadRequest, NotFound
from getnet.services.customers import Customer, Service
from getnet.services.service import ResponseList


@pytest.mark.vcr
def test_create(client: Client, customer_sample: dict):
    customer_sample["document_number"] = "01234567888"

    customer = Service(client).create(Customer(**customer_sample))

    assert isinstance(customer, Customer)
    assert customer_sample.get("customer_id"), customer.customer_id


@pytest.mark.vcr
def test_invalid_create(client: Client, customer_sample: dict):
    with pytest.raises(BadRequest) as excinfo:
        Service(client).create(Customer(**customer_sample), False)

    assert "400" == excinfo.value.error_code


@pytest.mark.vcr
def test_create_return_if_already_exists(client: Client, customer_sample: dict):
    customer = Service(client).create(Customer(**customer_sample), True)

    assert isinstance(customer, Customer)
    assert customer_sample.get("customer_id"), customer.customer_id


@pytest.mark.vcr
def test_get(client: Client, customer_sample: dict):
    customer_sample["customer_id"] = "test_integration_get"
    customer_sample["document_number"] = "01234567811"
    service = Service(client)
    created_customer = service.create(Customer(**customer_sample))

    customer = service.get(created_customer.customer_id)

    assert isinstance(customer, Customer)
    assert created_customer == customer
    assert created_customer.customer_id == customer.customer_id


@pytest.mark.vcr
def test_invalid_get(client):
    with pytest.raises(NotFound) as excinfo:
        Service(client).get("14a2ce5d-ebc3-49dc-a516-cb5239b02285")

    assert "404" == excinfo.value.error_code


@pytest.mark.vcr
def test_all(client):
    customers = Service(client).all()
    assert isinstance(customers, ResponseList)
    assert 1 == customers.page
    assert 100 == customers.limit
    assert customers.total is not None


@pytest.mark.vcr
def test_all_not_found(client):
    cards = Service(client).all(document_number="01234567855")
    assert 0 == cards.total
