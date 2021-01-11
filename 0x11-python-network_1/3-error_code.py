#!/usr/bin/python3
""" Module to sends a request to the URL
    and displays the body of the response
"""

from urllib import error, request
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            page = response.read().decode("utf-8")
        print(page)
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
