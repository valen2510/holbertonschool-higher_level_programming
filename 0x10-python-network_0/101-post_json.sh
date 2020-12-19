#!/bin/bash
#  Script that sends a JSON POST request and displays the body of the response.
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
