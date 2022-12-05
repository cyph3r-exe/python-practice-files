import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Monkul@2004',
)

print(mydb)
mydb.close()