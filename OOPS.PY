class student:
    'comment in base class for all student'
    studentcount = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        student.studentcount = student.studentcount + 1
    def display(self):
        print("total student %d"%student.studentcount)
    def displaystudent(self):
        print("Name: ",self.name,"Marks :",self.marks)
# access by it object
stu1 = student("Raja",94)
stu2 = student("Jitesh",96)
stu1.displaystudent()
stu2.displaystudent()
print("Total student is %d "%student.studentcount)

# how to change the marks 94 to 49 and 96 to 69
stu1.marks = 49
stu2.marks = 69
stu1.displaystudent()
stu2.displaystudent()
# doc sring comment how to implement
print("student.__doc__",student.__doc__)
print("student.__name__",student.__name__)
print("student.__module__",student.__module__)
print("student.__bases__",student.__bases__)
print("student.__dict__",student.__dict__)



    