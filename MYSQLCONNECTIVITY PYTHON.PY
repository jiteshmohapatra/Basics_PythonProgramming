

#For connectivity we are doing write a resource variable that is
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123")
# Now i have done this
if mycon.is_connected(): 

    print("successfully connected")
cur = mycon.cursor()
cur.execute("CREATE DATABASE db1")'''
# for connectivity is done this code is comment out
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")

str = "CREATE TABLE book(bookid integer(4),title varchar(20),price float(5,2))"
cur = mycon.cursor()
cur.execute(str)'''
#how do i insert values in table
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")
str = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
b1 = (101,"Python3",345)
cur = mycon.cursor()
cur.execute(str,b1)
mycon.commit()'''
#Insert multiple values
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")
str = "INSERT INTO book(bookid,title,price) VALUES(%s,%s,%s)"
books = [(102,"Java",563),(103,"PHP",849),(104,"AI",999)]
cur = mycon.cursor()
cur.executemany(str,books)
mycon.commit()'''
# extracting data

'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")
str = "SELECT * from book"
cur = mycon.cursor()
cur.execute(str)
result = cur.fetchall()
for res in result:
    print(res)'''
   
# UPDATE TABLE RECORDS
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")
str = "UPDATE book SET price=price-30 WHERE price>500"
cur = mycon.cursor()
cur.execute(str)
mycon.commit() '''  
# delete records
'''mycon = mysql.connector.connect(host="localhost",user="root",passwd="Nsti123",database="db1")
str = "DELETE from  book WHERE title ='PHP'"
cur = mycon.cursor()
cur.execute(str)
mycon.commit()'''


# How to delete the record










