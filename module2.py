'''import module1
module1.fn1()
module1.fn2() '''   # suppose i want to execute one function in module1
from module1 import fn3
fn3()
# suppose i want to print two function
from module1 import fn3,fn1
fn3()
fn1()
#OR 
from module1 import *
fn3()
fn2()
fn1()

# how to renaming

'''import module1 as  j
j.fn3()''' # this is rename yhe module you can give the alius as clause name

import math
x = math.pi
print("the value of pi is %f"%x)

# how to see what function inside math

from math import pi
#x = pi
print("the value of pi is %f"%pi)
print(dir(math)) # dir() function display all the function inside math module

print(math.factorial(5)) # these are the special function 
print(math.sqrt(625))
