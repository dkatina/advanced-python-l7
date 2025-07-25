import requests #Imports the request library that we installed, so that we can actually use it
import json #Imports builtin json package

def send_request():
    """Making a request to the JSONplaceholder API
    JSONplaceholder is a wonderful API for learning
    Basic requests.
    """
    resource = input("What would you like to see (users|posts|todos)")

    #Step 1: Define our URL and our endpoint (route)
    #                   URL                      Endpoint
    url = f'https://jsonplaceholder.typicode.com/{resource}'


    #Step 2: Make the request which will return a response object
            #HTTP method |
    response = requests.get(url)


    #Step 3: Check what we got back
    print("Status Code: ", response.status_code)
    print("Raw response: ", response.text)

    #Step 4: Parse JSON data (make it something useful in python)
    if response.status_code == 200: #Checking for successful request
        data = response.json() #Convert JSON into Python dict
        print(data)


send_request()