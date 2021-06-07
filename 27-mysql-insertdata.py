#!/bin/python3
# The above line is called as HashBang or ShBang line

import mysql.connector

mysql_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin@mysql", database = "employee")

print(mysql_conn)

cur = mysql_conn.cursor()

insdata = "insert into emp(name,id, role) values (%s, %s, %s)"
val = ("Shivani", 10012, "Developer")

try:
  cur.execute(insdata, val)
  mysql_conn.commit()
except:
  mysql_conn.rollbac()

print(cur.rowcount,"record inserted")

mysql_conn.close()

