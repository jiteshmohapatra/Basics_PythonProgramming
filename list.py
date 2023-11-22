# SOME BASICS OF LIST (IMPORTANT)

mylist = [5,7,9,'hello',9,10]
print(mylist[4]) # this one is list

mylist1 = [5,7,9,'hello',['ok','hello'],9,10]
print(mylist1[3]) # this one is multilist that is with in another list

# suppose i want to access hello ka O character
print(mylist[3][4]) # it will show answer hello ka O character

mylist = [1,2,3,5,"jitesh",10.5,10.2,"Mohapatra","raja"]

print(mylist[:5])
print(mylist[-6:-4])# ist will come start index then last index no -1
print(mylist[-4:-1])
print(mylist[0:-1])
print(mylist[-4:-2])

# how to reverse a list in python 
mylist.reverse()
print(mylist)

# how to use append function very important

mylist.append("Nsti bhubaneswer") # append function adding a elements to the end
print(mylist)

# how to use count function

x = mylist.count(3) # it wll count which times 3 are written in mylist variable
print(x)

#Lets try out SORT function 

mylist1 = [1,2,5,6,10,40,12,13,14,12,8,3,7,9,1,5,2,7]
mylist1.sort()
print(mylist1) # it will sort in ascending order

mylist2 = ["hello","hii","welcome","excellent","wow","hello","hii"]
y = mylist2.count("hello")
print(y)



#Practice For Exam python list and Dictionary


mylistnew = [1,2,3,"Peter","raja","peter",25,36,["Rajakumar",10.2,"Peter joy"]]
print(mylistnew)



print("/nhello")

'''example = "snow world"
example[3] = 's'
print(example)'''
'''print("hello"+1+2+3)
'''

'''print("*","abcdef".center(7),"*")'''
print("xyyzxyzxzxyy".count('xyy', 2, 11))
print("Hello {1} and {0}".format('bin', 'foo'))
print('The sum of {0} and {1} is {2}'.format(2, 10, 12))
print('The multiplication of {0} and {1} is{2} '.format(10,20,200))
print("ab".isalpha())
print('1.2'.isnumeric())
print('a'.maketrans('ABC', '123'))
print('xyyxyyxyxyxxy'.replace('xy', '12', 100))
print('abcd'.translate({'a': '1', 'b': '2', 'c': '3', 'd': '4'}))
set1 = set() # this one is to create empty set