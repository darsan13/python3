#!/bin/python3
# The above line is called as HashBang or ShBang line

import mysql.connector

mysql_conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "admin@mysql")

print(mysql_conn)
