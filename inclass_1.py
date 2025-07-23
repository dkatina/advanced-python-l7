import requests
import json

def get_random_dog():
    """
    Get a random dog picture and print it to the terminal
    
    API Endpoint: https://dog.ceo/api/breeds/image/random
    Look at the documentation to see the response format!
    """
    url = 'https://dog.ceo/api/breeds/image/random'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Random dog image: ", data['message'])


# Test your function
get_random_dog()