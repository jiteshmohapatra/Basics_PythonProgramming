'''a= int(input("Enter the celcius"))
res = (a*9/5)+32
b = int(input("enter a value in farenheit"))
res1 = b-32*5/9
print("The result in celcius to farhneit is ",res)
print("The result in farenheit to celcius is",res1)
'''

import mysql.connector
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123")
if mycon.is_connected():
    print("Successfully connected")

cur = mycon.cursor()
cur.execute("CREATE DATABASE ibmdb2")'''
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str = "CREATE TABLE cloud(cloudid integer(4),title varchar(20),price float(5,2))"
cur = mycon.cursor()
cur.execute(str)'''
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str = "INSERT INTO cloud(cloudid,title,price) VALUES(%s,%s,%s)"
c1 = (1011,"MACHINE LEARNING",599)
cur = mycon.cursor()
cur.execute(str,c1)
mycon.commit()'''
# how to insert multiple documents use executemany function
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str = "INSERT INTO cloud(cloudid,title,price) VALUES(%s,%s,%s)"
b1 = [(1012,"Hadoop",699),(2003,"Spark",499),(2004,"AI",64),(2005,"Chatgpt",899)]
cur = mycon.cursor()
cur.executemany(str,b1)
mycon.commit()'''
# how to extracting the data 
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str="SELECT * from cloud"
cur = mycon.cursor()
cur.execute(str)
result = cur.fetchall()
for res in result:
    print(res)'''

# how to update the table data 
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str ="UPDATE cloud set price=price-50 WHERE price>500"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()'''
# how to delete the records
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="ibmdb2")
str ="DELETE from cloud WHERE title = 'MACHINELEARNING' "
cur = mycon.cursor()
cur.execute(str)
mycon.commit()'''
for i in range(1,6):
    print(i)
print('*')
print('**')
print('***')
print('****')
print('****')