#!/usr/bin/python3
"""Sends a POST request with a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    url_param = {'email': email}

    req = requests.post(url, data=url_param)
    print(req.text)
