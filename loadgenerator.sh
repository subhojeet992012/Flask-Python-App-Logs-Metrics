#!/bin/bash

# Define an array of URLs
URLS=(
    "http://192.168.32.137:5000/static/sample.html"
    "http://192.168.32.137:5000/"
    "http://192.168.32.137:5000/metrics"
    "http://192.168.32.137:5000/fail"
)

# Infinite loop to keep hitting random URLs
while true; do
    # Select a random URL from the array
    RANDOM_URL=${URLS[$RANDOM % ${#URLS[@]}]}

    # Send a request using curl
    echo "Hitting: $RANDOM_URL"
    curl -s -o /dev/null -w "Response Code: %{http_code}\n" "$RANDOM_URL"

    # Sleep for a random time (1-5 seconds) before the next request
    sleep $((RANDOM % 5 + 1))
done

