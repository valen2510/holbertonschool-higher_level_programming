#!/usr/bin/python3
""" Module to fetch https://intranet.hbtn.io/status
    with urlib
"""

from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        data = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(data), data, data.decode("utf-8")))
