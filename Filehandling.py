'''
1)file name
2)Access_mode = r,r+,w,w+,a,a+ 
r = read mode
r+ = it is opening for the file for reading ane writting
w = opening file for writting
w+ = for reading and writting existing file is over write if it is open
a = append mode that is add 
a+= reading and writting
in python you can operate the file in binary mode rather than text mode
that is = rb,rb+,wb,wb+,ab,ab+
buffering = You are storing the data in a temporaryly until it loads properly


'''

file1 = open("demofile.txt","w") # opening file
file1.write("We are learning python file handling")
file1.close# closing a file