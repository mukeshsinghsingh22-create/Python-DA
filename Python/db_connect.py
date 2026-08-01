import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mukesh@2026"        
)
print(mydb)