getnet-python
=========
#### This project is a fork of [Getnet-py](https://github.com/ramon/getnet-py) 
#### This project provider a SDK to handler Getnet API.

Installation
------------

To install getnet-py you can use pip:

    $ pip install getnet-python

or pipenv:

    $ pipenv install getnet-python

    
Usage
-----

#####  For use this library the following information is needed:
 
 * Seller ID
 * Client ID
 * Client Secret
 
#####  The following environments are supported:

 * Sandbox
 * Homolog
 * Production
 
#####  At moment, we have support to the following services:

 * Token
 * Payments
   * Credit Card
 

Instancing the client
```python
from getnet import Environment, Client

client = Client("seller_id", "client_id", "client_secret", Environment.SANDBOX)
client.auth() # Optional, will be executed if needed
``` 

# Using the Services
### Examples

##### Consult Card BIN Informations
```python
card_bin = client.card_bin("515590") # Card related information and Status
```

### Customer
```python
customer_service = client.customer_service()
```
#### Create Customer
```python
customer_data = client.customer(
    {
        "first_name":"Joao",
        "last_name":"Pedro da Silva",
        "document_type":"CPF",
        "document_number":"77261241563",
        "birth_date":"1988-04-08",
        "phone_number":"5575999999999",
        "celphone_number":"5575999999999",
        "email":"fabvitor@test.com",
        "observation":"Test CLient",
        "customer_id":"77261241563", # or uuid4
        "seller_id":"6eb2412c-165a-41cd-b1d9-76c575d70a28",
        "address":{
            "street": "Rua Test",
            "number": "40",
            "complement": "Casa",
            "district": "Centro",
            "city": "São Paulo",
            "state": "SP",
            "country": "Brasil",
            "postal_code": "77019098",
        },
    }
)

customer = customer_service.create(customer_data)

```
#### Get Customer
```python
customer = customer_service.get("77261241563")
```
#### List All Customers Saved in Getnet
```python
customers = customer_service.all()
```
##### Tokenizing a Credit Card
```python
token = client.generate_card_token("5155901222280001", customer.customer_id)
token.number_token # token genered in getnet
```

##### Verify a Credit Card
```python
card_verified: bool = client.card_verified(
    number_token=tokenizado.number_token,  
    expiration_month="12",
    expiration_year="28"
    cardholder_name="JOAO DA SILVA",
    brand="Mastercard",
    security_code="123",
) # True or False

```
### Generate a Credit Card
```python
payment_card = client.credit_card(
    number_token=tokenizado.number_token,  
    cardholder_name="JOAO DA SILVA",
    security_code="123",
    brand="Mastercard",
    expiration_month="12",
    expiration_year="28"
    )
```
### Generate a Order
```python
payment_order = client.order("12345") 
```

### Generate a Payment Customer
```python
payment_customer = client.customer(customer) 
```

### Generate a Credit Card Payment
```python
payment = client.create_credit_transaction(
    amount="1000",
    delayed=False,
    pre_authorization=True,
    save_card_data=False,
    transaction_type="FULL",
    number_installments=1,
    order=payment_order,
    customer=payment_customer,
    card=payment_card,
    shipping_address={
        "street": "Rua Test",
        "number": "40",
        "city": "São Paulo",
        "state": "SP",
        "postal_code": "77019098"
    }, # The user's address may be different from the address registered with the consumer
)
    
payment_id = payment.payment_id # ID
status = payment.status # AUTHORIZED
```

### Adjust a Payment Amount
```python
payment_ajusted = client.adjust_credit_transaction(payment_id, "2000")
payment_ajusted.status # APROVED
```

### Capture a Credit Card Payment
```python
captured_payment = client.capture_credit_transaction(payment_id, "2000")
captured_payment.status # CONFIRMED
```

### Cancel a Credit Card Payment
```python
canceled_order = client.cancel_credit_transaction(payment_id)
canceled_order.status # CANCELED
cancel_payment_credit.credit_cancel.message # "Credit transaction cancelled sucessfully"
```
