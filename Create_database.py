
import mysql.connector

mydb = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "Hamzaeq786f#",
   database = "petrolpump_management"
)

c = mydb.cursor()

# c.execute("CREATE DATABASE petrolpump_management")