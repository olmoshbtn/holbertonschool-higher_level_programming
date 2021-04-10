#!/usr/bin/python3
"""List 10 commits (newest to oldest) of the repo "rails" by the user "rails"
"""

if __name__ == "__main__":
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    req = requests.get(url)
    data = req.json()
    i = 0
    while len(data) > i and i < 10:
        print(data[i].get('sha'), end=': ')
        print(data[i].get('commit').get('author').get('name'))
        i += 1
