#!/usr/bin/python3
"""Sends a request and shows if there is an HTTP error
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
        print(req.text)
    except:
        print("Error code: {}".format(req.status_code))
