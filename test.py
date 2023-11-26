import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'

# GET1
user_id = 1
response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
pprint.pprint('GET User')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.json())
pprint.pprint(response.text)
pprint.pprint("__________________________________________")

# POST1
data = {'name': 'Leonard'}
response = requests.post(f'{BASE_URL_PETSTORE}/user', json=data)

pprint.pprint('POST User{Data}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.json())

dict_text = json.loads(response.text)
user_id = dict_text['message']

pprint.pprint("__________________________________________")

# DELETE1
response = requests.delete(f'{BASE_URL_PETSTORE}/user/{user_id}')

pprint.pprint('DELETE user{Id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/user/{user_id}')
pprint.pprint(f'GET {user_id}')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint("__________________________________________")

# PUT1
updated_user_data = {
    'id': 1,
    'username': 'newuser_updated',
    'firstName': 'UpdatedFirstName',
    'lastName': 'UpdatedLastName',
    'email': 'updated@example.com',
    'phone': '9876543210'
}

response = requests.put(f'{BASE_URL_PETSTORE}/user/1', json=updated_user_data)
pprint.pprint('PUT User{Data}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)


# GET2
order_id = 2
response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
pprint.pprint('GET order{id}')

pprint.pprint(response.url)
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint(response.json())
pprint.pprint("__________________________________________")

# POST2
data = {'status': 'placed'}
response = requests.post(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=data)

pprint.pprint('POST order{id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint("__________________________________________")

# DELETE2
response = requests.delete(f'{BASE_URL_PETSTORE}/store/order/{order_id}')

pprint.pprint('DELETE order{id}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/store/order/{order_id}')
pprint.pprint(f'GET {order_id}')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint("__________________________________________")

# PUT2
updated_order_data = {
    "id": 2,
    "petId": 1,
    "quantity": 0,
    "shipDate": "2025-03-05T11:45:38.885+0000",
    "status": "placed"
}

response = requests.put(f'{BASE_URL_PETSTORE}/store/order/{order_id}', json=updated_order_data)
pprint.pprint('PUT Order{data}')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)