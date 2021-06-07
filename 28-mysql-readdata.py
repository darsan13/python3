#!/bin/python3
# The above line is called as HashBang or ShBang line

import mysql.connector

mysql_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin@mysql", database = "employee")

print(mysql_conn)

cur = mysql_conn.cursor()

try:
  cur.execute("select * from emp")
  rows = cur.fetchall()
except:
  mysql_conn.rollbac()

for r in rows:
  print(r)

mysql_conn.close()

