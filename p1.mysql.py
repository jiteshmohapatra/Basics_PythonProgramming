import mysql.connector
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123")
if mycon.is_connected():
    print("Successfully connected")
cur = mycon.cursor()
cur.execute("CREATE DATABASE ibmdb5")'''

# Create table

'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "CREATE TABLE it(Dep_id integer(5),Dep_name varchar(20),No_Of_Employee integer(5),Financial_year YEAR(4))"
cur = mycon.cursor()
cur.execute(str)'''
# hOW TO CHNAGE THE DATA TYPE OF A COLUMN
'''mycon = mysql.connector.Connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "ALTER TABLE it MODIFY Financial_year YEAR"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()
'''
# insert The data into the table


'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "INSERT INTO it(Dep_id,Dep_name,No_Of_Employee,Financial_year)VALUES(%s,%s,%s,%s)"
b1 = (1001,"Customer Service",15,2023)
cur = mycon.cursor()
cur.execute(str,b1)
mycon.commit()'''


# How to insert Mutiple data in a given table

'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "INSERT INTO it(Dep_id,Dep_name,No_Of_Employee,Financial_year)VALUES(%s,%s,%s,%s)"
b1 = [(1002,"HR",12,2023),(1003,"Accounts",16,2022),(1004,"Store",5,2021)]
cur = mycon.cursor()
cur.executemany(str,b1)
mycon.commit()
'''

#How to fetch all data.
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "SELECT * FROM it"
cur = mycon.cursor()
cur.execute(str)
result = cur.fetchall()
for res in result:
    print(res)
'''


# How to Update the table record

mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")
str = "UPDATE it set No_Of_Employee = 25 WHERE No_Of_Employee = 12"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()


mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb5")

str = "DELETE FROM it WHERE Financial_year = 2021"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()


# SUCCESSFULLY DONE MYSQL WITH PYTHON CONNECTIVITY 
