def show(x,y):
    if x >y:
        z = x
    else:
        z = y
    while(True):
        if((z % x==0) and (z % y== 0)):
            show =z
            break
        z+= 1
    return show
x = int(input("enter 1st integer"))
y = int(input("enter 2nd integer"))
res = show(x,y)
print("The LCM of two numbers is ",res)

        
