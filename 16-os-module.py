#!/bin/python3
# The above line is called as HashBang or ShBang line
import os

newdir = "devopshublab"
mode = 777
path = "/root/devopshub_lab"


def current_path():
  print("My current working direcotry before")
  print(os.getcwd())
  print()

current_path()

os.chdir('../')

current_path()

os.rmdir(newdir)
os.mkdir(newdir, mode)
print("Directory '% s' created" % newdir)

dir_list = os.listdir(path)

print("Files and diecotries in '", path, "' :")
print(dir_list)
