import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password123",
    database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("select name from tablename")
results= mycursor.fetchall()
results= mycursor.fetchone()

for i in mycursor:
    print(i)

mycursor.execute("select name from tablename")
results= mycursor.fetchone()

for row in results:
    print(row,'\n')

query= "insert into employee(name,sal) value(%s,%s)"
employees =[("chakra",9000),("chakri",10000),("chakram",18000)]
mycursor.executemany(query,employees)
mydb.commit()

queryupd="UPDATE employee SET sal=12000 where name='chakri'"
mycursor.execute(queryupd)
mydb.commit()

delquery ="Delete from employee where name='chakra'"
mycursor.execute(delquery)
mydb.commit()

