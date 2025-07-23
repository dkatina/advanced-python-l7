import requests
import json
#POST requests: are requests to send information to our backend to be stored in our database

#How do we send that info?

#We attatch it, by adding to the body of the request

#GET Request:
#http://api.example.com/endpoint

#POST Resquest:
#url: http://api.example.com/endpoint
#Body: {"Title": "My new Post": "userID": 1} Information that we are attatching to the request


def create_new_post():
    """Endpoint to send a POST request to the JSONplaceholder API"""

    url = 'https://jsonplaceholder.typicode.com/posts'

    #Creating request body
    post_data = {
        "title": "My first Post",
        "body": "Super happy to be a new user on Fakebook",
        "userId": 1
    }

    #Sending a post request

    response = requests.post(url, json=post_data)

    if response.status_code == 201: #checking for a successful creation
        data = response.json()
        print(f"User id: {data['userId']} has successfully posted, Title: {data['title']}")


create_new_post()