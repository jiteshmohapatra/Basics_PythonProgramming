class superclass:
    def method1(self):
        print("Inside parent class method")

class childclass(superclass):
    def method1(self):
        print("inside child class method")

x = childclass() 
x.method1() #This is called method overriding because same function can be called inside child class it can over ride it
        