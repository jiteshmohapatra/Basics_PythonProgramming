#Find the maximum of two numbers 
'''a =2
b =4
if a>=b:
    print("The number a is maximum")
else:
    print("the number b is maximum")'''
#or
'''def maximum(a,b):
    if a>=b:
        print("The number a is maximum")
    else:
        print("The number b is maximum")
a =25
b =20
maximum(a,b)'''
'''a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
c = int(input("enter 3rd number"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("C is greater")'''
'''a = int(input("Enter a number"))
if a<0:
   print("The number is negetive")
else:
   print("the number is possitive")'''
'''a =int(input("Enter a number"))
while a>20:
      print(a)
      a=a-1
print("out side the while loop")'''

'''p1 = [5,8,6,9,7,3]
for x in p1:
    print(x)'''

#or range function is use
'''for x in range(10,20):
    print(x)'''

'''for x in range(10,20):
    if x==15:
        break
    print(x)'''

'''for x in range(10,20):
    if x==15: # it will print all number except 15
        continue
    print(x)'''

#what is pass statement 
for x in range(10,20):
    if x==15: # just doing nothing but it will execute that line but which is nothing
        pass
    print(x)



    
