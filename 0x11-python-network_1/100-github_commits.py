#!/usr/bin/python3
"""Module to list 10 commits of the repository “rails” by the user “rails”
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url).json()
    for commit_list in response[:10]:
        commit = commit_list.get('sha')
        author_name = commit_list.get('commit').get('author').get('name')
        print("{}: {}".format(commit, author_name))
