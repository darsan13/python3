#!/bin/python3
# The above line is called as HashBang or ShBang line

class Parrot:

  def fly(self):
    print("Parrot can fly")

  def swim(self):
    print("Parrot can not swim")

class Penguin:
  
  def fly(self):
    print("Penguin can not fly")

  def swim(self):
    print("Penguin can swim")


def flying_test(bird):
  bird.fly()

def swim_test(bird):
  bird.swim()


blue = Parrot()
peggy = Penguin()

flying_test(blue)
flying_test(peggy)

swim_test(blue)
swim_test(peggy)

