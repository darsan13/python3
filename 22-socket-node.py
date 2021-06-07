#!/bin/python3
# The above line is called as HashBang or ShBang line

import socket

host='192.168.2.40' #client ip
port = 4005

server = ('192.168.2.20', 4000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

message = input("-> ")
while message !='q':
  s.sendto(message.encode('utf-8'), server)
  data, addr = s.recvfrom(1024)
  data = data.decode('utf-8')
  print("Received from server: " + data)
  message = input("-> ")
s.close()

