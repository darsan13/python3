#!/bin/python3
# The above line is called as HashBang or ShBang line

class Computer:

  def __init__(self):
    self.__maxprice = 900

  def sell(self):
    print("Selling Price: {}.".format(self.__maxprice))

  def SetMaxPrice(self, price):
    self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()


c.SetMaxPrice(1000)
c.sell()
