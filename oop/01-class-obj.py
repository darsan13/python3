#!/bin/python3
# The above line is called as HashBang or ShBang line

class myclass:
   x = 5

myobj = myclass()

print(myobj.x)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

#custom function or method inside the class
  def greet(self):
    print("Hello my name is ", self.name)
    print("I am ", + self.age)

   

p1 = Person("Darsan", 39)

print(p1.name)
print(p1.age)


p1.greet()
