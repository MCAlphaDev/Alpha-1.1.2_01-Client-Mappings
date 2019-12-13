@echo off
py scripts/setupmapclient.py
java -jar enigma.jar --jar=./dontpush/client.jar --mappings=./mappings/