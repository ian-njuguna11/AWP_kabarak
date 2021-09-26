import mysql.connector

import pymysql

pymysql.install_as_MySQLdb()

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb)