class base:
    basevar = 50
    def __init__(self):
        print("Inside constructor")
    
    def basemethod(self):
        print("inside base method")

    def setAttr(self,var1):
        base.basevar = var1

    def getAttr(self):
        print("Base variable:",base.basevar)

class derived(base):
    def __init__(self):
        print("Inside child class constructor")

    def childmethod(self):
        print("Inside child method.")

obj = derived()
obj.childmethod()
obj.basemethod()
obj.setAttr(525)   #it set the value that is setattr
obj.getAttr()
#we can also access the base class we use obj.base()


        


        
   