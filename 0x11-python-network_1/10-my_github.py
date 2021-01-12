#!/usr/bin/python3
""" Module for Github credentials (username and password),
    that uses the Github API to display id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(argv[1])
    token = argv[2]
    auth_header = {'Authorization': 'token {}'.format(token)}
    response = requests.get(url, headers=auth_header)
    print(response.json().get('id'))
