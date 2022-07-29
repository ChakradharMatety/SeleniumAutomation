import mysql.connector

# mydb = mysql.connector.connect(host='127.0.0.1',user='root',password='root',
# database='classicmodels',auth_plugin='mysql_native_password')
mydb = mysql.connector.connect(host='127.0.0.1', user='root', password='root')
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("show databases")
for db in mycursor:
    print(db)
mycursor.execute("use classicmodels")
# mycursor.execute("DELETE FROM offices where officeCode=10")

# query = "INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) " \
#         "values(10,'Zurich','+91 9063965369','NULL','Floor 9','TA','SWISS','040299','UK')"
# query = "INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) " \
#         "values(10,'Zurich','+91 9063965369','','Floor 9','TA','SWISS','040299','UK')"
# mycursor.execute(query)
# mydb.commit()

mycursor.execute("select *from payments")
result = mycursor.fetchone()
print(result)
results = mycursor.fetchall()
print(results)

for data in results:
    print(data)

# mycursor.execute("select *from employees where employeeNumber='1088'")
# results = mycursor.fetchone()
# print(results)
#
# mycursor.execute("select *from offices")
# results = mycursor.fetchall()
# # print(results)
# for data in results:
#     print(data)
# print(results[0][1])
#
# query = "INSERT INTO payments(customerNumber,checkNumber,paymentDate,amount) " \
#         "values(497,'CHK04026','2022-07-16',1116.09)"
# paymentsdata = [(497, "NULL", "NULL", 1111.05)]
# query = "INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) " \
#         "values(10,'Zurich','+91 9063965369','','Floor 9','TA','SWISS','040299','UK')"
# query = "UPDATE offices SET territory='SWISS' where officeCode=8"
# query = "DELETE FROM offices where officeCode=10"
#
#
