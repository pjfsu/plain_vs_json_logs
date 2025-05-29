#!/bin/bash

for i in {1..1111}; do
    rand=$((RANDOM % 3))  # Generates a random number between 0 and 2

    case $rand in
        0) request="info";;
        1) request="warning";;
        2) request="error";;
    esac

    curl -s "http://localhost:5000/$request" # Silent mode
done
