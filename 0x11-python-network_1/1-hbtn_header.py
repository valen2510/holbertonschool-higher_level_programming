#!/usr/bin/python3
""" Module to sends a request to the URL
    and displays the value of the X-Request-Id
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        response_info = response.info()
    print(response_info.get('X-Request-Id'))
