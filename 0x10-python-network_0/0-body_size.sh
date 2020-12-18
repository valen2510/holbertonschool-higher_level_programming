#!/bin/bash
# Script that sends a request to that URL, and displays the size of the body of the response.
curl -so /dev/null "$1" -w "%{size_download}\n"
