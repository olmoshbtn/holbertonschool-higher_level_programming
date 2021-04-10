#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        data = response.read()

    data_type = type(data)
    data_utf8 = data.decode('utf8')

    print("Body response:")
    print("\t- type: {}".format(data_type))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data_utf8))
