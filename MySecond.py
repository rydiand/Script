import time
import os
from datetime import datetime
#functions
def path1():
    file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
    print(file_path)

def time1():
    
    mod_time = os.stat('C:\\users\\torben\\downloads\\desktop.ini').st_mtime
    real_time = datetime.fromtimestamp(mod_time)
    return real_time
#

fname = "Torben"
lname = "Rydiander"
print("Hello World and",fname, lname)

# time.sleep(5)
# func1()
os.system('dir')
#os.chdir('/u/g22392/gitrepo/test')
# os.system('dir')
# os.getpid()
# print(dir(os))
# print(dir(os.path))
# print(os.path.curdir())
print(time1())
path1()
    


def func1():
    marks = 75
    if (marks > 80):
        print("A")
    elif (marks > 60):
        print("B")
    elif (marks > 40):
        print("C")
    else:
        print("D")

def func2():
    fname = input("State your first name: ")
    lname = input("State your last name: ")
    print("Hello Again " + fname)
    print("I like typing this.")
    print("This is fun.")
    print('Yay! Printing.')
    print("I'd much rather you 'not'.")
    print('I "said" do not touch this.')
    print(8 // 3)
    print(8 / 3)
    print(8 % 3)
    x = 55
    print(x)
    x/=4
    print(x)
    # fname*=2
    print("Bye",fname,lname,", leave you in 5 sec.")
    time.sleep(5)
