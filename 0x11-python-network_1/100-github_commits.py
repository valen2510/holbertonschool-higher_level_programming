#!/usr/bin/python3
"""Module to list 10 commits of the repository “rails” by the user “rails”
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url).json()
    for i in range(10):
        commit = response[i].get('sha')
        author_name = response[i].get('commit').get('author').get('name')
        print("{}: {}".format(commit, author_name))
