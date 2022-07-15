import mysql.connector

mydb=mysql.connector.Connect(host="",user="",password="")
mycursor=mydb.cursor()

mycursor.execute("select age from tablename")
results=mycursor.fetchall()
results=mycursor.fetchone()
for i in results:
    print(i)

query = "insert INTO tablename(name,value) values(%s,%s)"
employee=[("chakra",9000),("chakri",9000),("chakram",9000)]
mycursor.executemany(query,employee)
mydb.commit()

# SELECT *from tablename
# SELECT *from tablename ORDER BY user_id
# SELECT name,agr from tablename
# SELECT name,agr from tablename GROUP BY col ORDER BY col
# SELECT SUM(salary) FROM tablename
# SELECT COUNT(*) From tablename
# SELECT DISTINCT column from tablename
# INSERT INTO tablename(name,age) VALUES(%s,%s)
# employee=[("chakra",26),("chekra",30),("chakri",32)]
# UPDATE tablename SET name='chakradhar' WHERE id="999"
# UPDATE tablename SET name='chakradhar',age="29 WHERE id="999"
# UPDATE tablename SET name='chakradhar',age="29 WHERE userid IN(999,555,666)
# DELETE FROM tablename
# DELETE FROM tablename WHERE id=999

# SELECT *FROM leftTable INNER JOIN rightTable ON leftTable.id=rightTable.id
# SELECT firstname,lastname,email FROM leftTable INNER JOIN rightTable ON leftTable.id=rightTable.id
#  and also can have where and order clause by col
# SELECT *FROM leftTable LEFT JOIN rightTable ON leftTable.id=rightTable.id
# SELECT *FROM leftTable RIGHT JOIN rightTable ON leftTable.id=rightTable.id
# SELECT *FROM leftTable FULL JOIN rightTable ON leftTable.id=rightTable.id