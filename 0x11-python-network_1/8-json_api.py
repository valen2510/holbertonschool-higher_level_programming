#!/usr/bin/python3
""" Module that ends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 0:
        value = {'q': argv[1]}
    else:
        value = {'q': ""}
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", value)
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print('No result')
    except Exception:
        print("Not a valid JSON")
