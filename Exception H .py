#Exception Handling
try:
    num = 5
    den = 0
    output = num/den
    print(output)
except:
    print("Error will come: den can not be o")

# Different way
# program is fine
try:
    evennos = [8,10,12,16,2,20]
    r = evennos[0]/0
    print(r)
    print(evennos[6])                           
except ZeroDivisionError:
    print("Denomitor can not be zero")
except IndexError:
    print("index out of bounds.")
except SyntaxError:
    print("error in syntax")
 # try with else

try:
    num = int(input("Enter a number"))
    assert num%2 == 0 # check the sanity of the program
except:
    print("not an even number")
else:
    reciprocal = 1/ num
    print(reciprocal)
finally:
    print('inside a finally block') # not an even number it will inside the finally block




           