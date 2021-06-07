#!/bin/python3
# The above line is called as HashBang or ShBang line

import mysql.connector

mysql_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin@mysql", database = "employee")

print(mysql_conn)

cur = mysql_conn.cursor()

try:
  dbs = cur.execute("create table emp(name varchar(20) not null, id int(20) not null primary key, role varchar(20) not null)")
except:
  mysql_conn.rollbac()

mysql_conn.close()

