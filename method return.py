class c1:
    def __init__(self):
        print("inside constructor")
    def calculate(self,x,y):
        res = x+y
        return res
c1obj = c1()
a1 = c1obj.calculate(20,30)
print("the result is %d"%a1)
        