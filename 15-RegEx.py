#!/bin/python3
# The above line is called as HashBang or ShBang line

import re

txt = "The rain is in spain"

x = re.search("^The.*spain$", txt)

print(x)
