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

##### Tokenizing a credit card
```python
token = client.generate_card_token("5155901222280001", "customer_21081826")
token.number_token # token genered in getnet
```

### Generate a credit card
```python
card = client.credit_card(
    number_token=tokenizado.number_token,  
    cardholder_name="JOAO DA SILVA",
    security_code="123",
    brand="Mastercard",
    expiration_month="12",
    expiration_year="28"
    )
```

### Generate a order
```python
order_id = "12345"
order = client.order(order_id) 
```

### Generate a customer
```python
customer_id = "12345"
customer = client.customer(order_id) 
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
    order=order,
    customer=customer,
    card=card
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
captured_payment = client.capture_credit_transaction(id_pagamento, "2000")
captured_payment.status # CONFIRMED
```

### Cancel a Credit Card Payment
```python
canceled_order = client.capture_credit_transaction(id_pagamento, "2000")
canceled_order.status # CANCELED
cancel_payment_credit.credit_cancel.message # "Credit transaction cancelled sucessfully"
```
