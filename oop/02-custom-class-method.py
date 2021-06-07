#!/bin/python3
# The above line is called as HashBang or ShBang line

class myclass:
   x = 5

myobj = myclass()

print(myobj.x)


class Person:
  def __init__(myparam, name, age):
    myparam.name = name
    myparam.age = age

#custom function or method inside the class
  def greet(objparam):
    print("Hello my name is ", objparam.name)
    print("I am ", + objparam.age)

   

p1 = Person("Darsan", 39)

print(p1.name)
print(p1.age)


p1.greet()
