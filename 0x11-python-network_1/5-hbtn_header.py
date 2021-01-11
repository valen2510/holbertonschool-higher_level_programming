#!/usr/bin/python3
""" Module to sends a request to the URL
    and displays the value of the X-Request-Id
"""

import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1]).headers
    print(response.get('X-Request-Id'))
