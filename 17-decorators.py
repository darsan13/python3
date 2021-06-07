#!/bin/python3
# The above line is called as HashBang or ShBang line

def make_pretty(func):
  def inner():
    print("I got decorated")
    func()
  return inner

@make_pretty
def ordinary():
  print("I am ordinary")


ordinary()
