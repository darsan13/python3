#!/bin/python3
# The above line is called as HashBang or ShBang line

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


p1 = Person("Priyadarsan", "Sahu")

print("From the parent class")
p1.printname()

class Student(Person):
  pass # Entire person class has been inherited
#  def __init__(self, fname, lname): #it will not inherit the __init__ from parent class


st1 = Student("Shivani", "P")

print("From the child class")
st1.printname()
