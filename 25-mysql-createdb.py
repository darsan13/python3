#!/bin/python3
# The above line is called as HashBang or ShBang line

import mysql.connector

mysql_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin@mysql")

print(mysql_conn)

cur = mysql_conn.cursor()

try:
  dbs = cur.execute("create database employee")
  dbs = cur.execute("show databases")
except:
  mysql_conn.rollbac()

for d in cur:
  print(d)

mysql_conn.close()

