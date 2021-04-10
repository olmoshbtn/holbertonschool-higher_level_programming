#!/usr/bin/python3
"""Displays the X-Request-Id header from an HTTP response
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    data = req.text
    print(req.headers.get('X-Request-Id'))
