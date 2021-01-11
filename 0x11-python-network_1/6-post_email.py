#!/usr/bin/python3
""" Module to send a POST request to the passed URL
    with the email, and displays the body of the response
"""


import requests
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    post_request = requests.post(argv[1], value).text
    print(post_request)
