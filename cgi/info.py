#!/usr/bin/env python3
import os
import sys

print("Content-Type: text/html\r")
print("\r")
print("<html><head><title>CGI Info</title></head><body>")
print("<h1>CGI is working</h1>")
print("<h2>Environment</h2><pre>")
for key, val in sorted(os.environ.items()):
    print("{} = {}".format(key, val))
print("</pre>")

body = sys.stdin.read()
if body:
    print("<h2>Request Body</h2><pre>")
    print(body)
    print("</pre>")

print("</body></html>")