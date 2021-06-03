#!/bin/python3
# The above line is called as HashBang or ShBang line

numbers = [4, 5, 7, 6, 9]

print("The items in the list are", numbers)

print(len(numbers))

print(numbers[1])
print(numbers[-1]) #prints the last number

#check if a 7 is present in the list

if 7 in numbers:
  print(" 7 is part of list")

# change the 3rd item to 8

numbers[2] = 8
print(numbers)

numbers.append("8")
print(numbers)

# remove an item

numbers.remove(9)
print(numbers)

#mylist = ["darsan", "39", "76.89"]
#print(mylist)
