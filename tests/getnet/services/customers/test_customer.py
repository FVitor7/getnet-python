from getnet.services.customers import Customer, Address


def test_address_conversion(customer_sample: dict):
    customer = Customer(**customer_sample)

    assert isinstance(customer.address, Address)
    assert (
        customer_sample.get("address").get("postal_code")
        == customer.address.postal_code
    )


def test_full_name(customer_sample: dict):
    customer = Customer(**customer_sample)

    sample_full_name = f'{customer_sample["first_name"]} {customer_sample["last_name"]}'

    assert sample_full_name == customer.full_name
