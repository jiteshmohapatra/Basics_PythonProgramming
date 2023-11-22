'''openfile = open("demofile.txt","r+")
str1 = openfile.read(15)
print("Read the string: ",str1)
openfile.close()'''

'''a = 10
b = 50
print("the value of a is {} and b is {}".format(a,b))'''
file_open = open("demofile.txt","r+")
str1 = file_open.read(25)
print("The string is :",str1)
# check to the current position
position = file_open.tell()
print("File current position",position)
# Reposition the file pointer at the beginning
position = file_open.seek(0,0)#0,0 means is beginning to end position suppose you(5,10) bi add kar sakte hai
str1 = file_open.read(22)
print("read again :",str1)
file_open.close()
list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)
i = 0 
while i < 5: 
      print(i) 
      i += 1 
      if i == 3: 
           break 
else: 
      print(0)
x = 5 
y = "hello" 
company = ['P','R','O','M','O','T','E']
for x in company:
    if x == "M":
        break
    print(x)
L = [lambda x: x ** 2,
lambda x: x ** 3,
lambda x: x ** 4] 
for f in L:
  print(f(3))
min = (lambda x, y: x if x < y else y)
min(101*99, 102*98)
print(2**3 + (5 + 6)**(1 + 1))
min = (lambda x, y: x if x < y else y)
print(min(101*99, 102*98))


