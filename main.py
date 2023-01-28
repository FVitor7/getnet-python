from getnet import Environment, Client
from decouple import config

seller_id = config('SELLER_ID')
client_id = config('CLIENT_ID')
client_secret = config('CLIENT_SECRET')
print(seller_id, client_id, client_secret)
client = Client(seller_id, client_id, client_secret, Environment.SANDBOX)

# TEST LOGIN
client.auth() # Optional, will be executed if needed
print(client.access_token)



# TEST CONSULT CARD TOKEN
number_token = response = client.generate_card_token(
    card_number="5155901222280001",
    customer_id="1234",
).number_token

print(number_token)
