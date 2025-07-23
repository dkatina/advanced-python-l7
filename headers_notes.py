import requests
import json

#========================= Headers ==========================

#Headers: are we store additional information about our request (data format, credentials)


def send_headers():

    url = 'https://reqres.in/api/users'

    my_headers = {
        "x-api-key": "reqres-free-v1"
    }

    response = requests.get(url, headers=my_headers)

    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data)


# send_headers()


def create_user():

    resource = input("what would you like to get")

    url = f'https://reqres.in/api/{resource}'

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    email = input("Give me your email: ")

    body = {
        "email": email,
        "first_name": "Dylan",
        "last_name": "Katizzy",
        "avatar": "N/A"
    }

    response = requests.post(url, headers=headers, json=body)

    print(response.status_code)
    print(response.json())

create_user()


