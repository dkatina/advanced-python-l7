import requests
import json

#============= Query Parameters

#Query parameters are another way for us to send information to our server

#However, query parameters are sent through the url itself

#example
#https://api.example.com/endpoint?userId=1

#query params come after the '?'
#- organized in key value pairs: key=value
#- often used in filter, sorting, sending quick data

def query_params():
    """Testing using query parameters, sending info through the url"""

    url = 'https://jsonplaceholder.typicode.com/posts'

    params = {
        "userId": 1
    }

    response = requests.get(url, params=params)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("UserId 1's post titles")
        for post in data:
            print('-', post['title'])


query_params()