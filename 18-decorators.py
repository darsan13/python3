#!/bin/python3
# The above line is called as HashBang or ShBang line

# Chaining Decorators

def star(func):
  def inner(*args, **kwargs):
    print("*" * 30)

    func(*args, **kwargs)
    print("*" * 30)
  return inner

def percent(func):
  def inner(*args, **kwargs):
      print("%" * 30)
      func(*args, **kwargs)
      print("%" * 30)
  return inner


@star
@percent
def printer(msg):
  print(msg)

printer("Welcome to DevOpsHub")

