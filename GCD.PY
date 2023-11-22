def gcd(x,y):
    gcd =1
    if x%y==0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd = k
            break
    return gcd
# print("The two number of gcd is :",gcd(48,18))
  
x = int(input("Enter 1st number"))
y = int(input("Enter second number"))
output = gcd(x,y)
print("These two numbers of gcd is ",output)

#OR using while loop

def calculate(a,b):
    z = a%b
    while z:
        a = b
        b = z
        z = a%b
    return b
a = int(input("Enter 1st integer"))
b = int(input("Enter 2nd integer"))
output1 = calculate(a,b)
print("The GCD of two integers is ",output1)

      
    

     

