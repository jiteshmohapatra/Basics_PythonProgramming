str1 = "OUTSTANDING"
#print(str1[5])
print(str1[-11])
# suppose want to print STAND how to print
print(str1[3:8])
print(str1[0:3])
print(str1[0:-8])
#str1[0] = "B"
#print(str1) # it will show error because of string manipulation is immutable 
print(str1*4) #it will print 4 times OUTSTANDING

x = "NSTI BHUBANESWAR"
#print(x)
#print("The name %s is very common" %x) # %s works like a placeholder
print("The name %s is very common" %'jitesh') #it will print the name jitesh is very common


print("names ending with %c is very common female name in india"%'A') # c for character
print("india is celebrating %d years of independence" %75)
yrs = 2023-1947
print("india will celebrate %d years of independence" %yrs) # this one is format specifier %d

a = float(input("Enter 1st number"))
b = float(input("Enter 2nd number"))
c = a*b
print("The product of 2 number is %f after doing operation" %c)
'''a =int(input("Ener The number"))
print("The number entered is %f" %a)'''


