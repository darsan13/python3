#!/bin/python3
# The above line is called as HashBang or ShBang line

import os

if os.path.exists("mynewfile.txt"):
  os.remove("mynewfile.txt")
else:
  print("The file is not available for delete")

