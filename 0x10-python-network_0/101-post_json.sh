#!/bin/bash
# Send a POST request to a URL using JSON data and display the response body
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
