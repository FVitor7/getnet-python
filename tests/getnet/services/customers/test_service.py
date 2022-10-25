from getnet import Client
from getnet.services.customers import Service, Customer
from getnet.services.service import ResponseList


def test_create(
    client_mock: Client, customer_sample: dict, customer_response_sample: dict
):
    client_mock.post.return_value = customer_response_sample

    service = Service(client_mock)
    customer = service.create(Customer(**customer_sample))

    assert isinstance(customer, Customer)
    assert customer_sample.get("customer_id") == customer.customer_id


def test_all(client_mock: Client, customer_response_sample: dict):
    client_mock.get.return_value = {
        "customers": [
            customer_response_sample,
            customer_response_sample,
            customer_response_sample,
        ],
        "page": 1,
        "limit": 100,
        "total": 3,
    }

    service = Service(client_mock)
    customers = service.all()

    assert isinstance(customers, ResponseList)
    assert 1 == customers.page
    assert 3 == customers.total
    assert customer_response_sample.get("customer_id") == customers[0].customer_id


def test_get(client_mock: Client, customer_response_sample: dict):
    client_mock.get.return_value = customer_response_sample

    service = Service(client_mock)
    customer = service.get(customer_response_sample.get("customer_id"))

    assert isinstance(customer, Customer)
    assert customer_response_sample.get("customer_id") == customer.customer_id
    client_mock.get.assert_called_once_with(
        "/v1/customers/{}".format(customer_response_sample.get("customer_id"))
    )
