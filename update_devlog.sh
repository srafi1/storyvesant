#! /bin/bash

echo "Who is this?"
read name
echo "What is the update?"
read update
echo "$name -- $(date)" >> devlog.txt
echo $update >> devlog.txt
