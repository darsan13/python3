#!/bin/python3
# The above line is called as HashBang or ShBang line

f = open("demofile.txt", "r")

#print(f.read())


#print("Reading line by line")
#print(f.readline())
#print(f.readline())
#print(f.readline())

for l in f:
  print(l)
