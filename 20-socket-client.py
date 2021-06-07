#!/bin/python3
# The above line is called as HashBang or ShBang line

import socket
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
print(s.recv(1024))
s.close()
