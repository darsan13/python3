#!/bin/python3
# The above line is called as HashBang or ShBang line

#x = lambda a : a +10
#print(x(8))

#x = lambda a,b : a * b
#print(x(5, 6))

#x = lambda a, b, c : a + b +c
#print(x(5, 6, 8))


def myfunc(n):
  return lambda a : a * n

double = myfunc(2)

print(double(11)) 

