#!/bin/python3
# The above line is called as HashBang or ShBang line

x = 500

def myfunc1():
  x = 300
  print(x)

def myfunc2():
  print(x)

myfunc1()
myfunc2()
print(x)
