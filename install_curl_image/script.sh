#!/bin/bash
while true
do
    echo "Input website:"
    read -r website; echo "Searching.."
    sleep 1; curl "http://$website"
done