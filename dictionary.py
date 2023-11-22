dict1 = {'name':'jitesh','age':23,'city':'bhubaneswar'}
#print(dict1['city'])
print(dict1)

# how to update the dictionary value
dict1['age']=22
print(dict1)
# how to add an item in dictionary
dict1['pin'] = 754160
print(dict1) # so this one completely added in the dictionary

# how to delete dictionary 
del dict1['city'] # lets say iwant to delete the city with the help of keyword
print(dict1)
# how to clear all the content inside the dictionary
dict1.clear()
print(dict1) # nothing there inside

# how to completely delete the dictionary so what to do
#del dict1
#print(dict1) # error is showing because the print dict1 is not exist so it is completely deleted

# IN PYTHON  THERE ARE NUMEROUS WELL STRUCTURED BUILT IN FUNCTION 

#ANONYMOUS FUNCTION
add = lambda arg1,arg2,arg3,arg4:arg1+arg2+arg3+arg4 # here lamda is an anonymous function so the use of lamda function the add variable is treated as function in this case
print(add(10,20,30,40))

#OR 
s = add(20,30,40,50)
print("The output of lamda function %d" %s)


