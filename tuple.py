# SOME BASICS OF TUPLE (IMPORTANT)
# 1) Tuple is also called immutable version of list 
# 2) list is mutable
# 3) Tuple is created inside parentheses

mytuple = ('welcome','great','wonderfull','wow','welcome')
print(mytuple)

# suppose i want to access wonderfull how to do it
print(mytuple[2])

# suppose i want to print ist three
print(mytuple[0:-1])

# count function in TUPLE
x = mytuple.count('welcome')
print(x)





# SORT function in TUPLE 

mytuple1 = (1,5,2,6,3,7,4,9,25,22,12,10,8,9)
res = mytuple1(sorted(mytuple1))
print('the sorted tuple are ',res)
