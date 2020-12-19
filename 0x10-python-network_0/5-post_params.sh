#!/bin/bash
# Script that sends a POST request to the passed URL, and displays the body of the response.
curl -s "$1" -X POST -d "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD"
