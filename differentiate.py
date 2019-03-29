#!/usr/bin/python3

##                                                ##
## program differentiates a user inputed function ##
##                                                ##
from math import *

print("")
print("This program finds the differential of a function using three-point derviative")
print("")

# get function
function = input("Enter a function f(x): ")

# if no user input, exit
if len(function) == 0:
    exit()

# create function from input
f = lambda x: eval(function)

# get x value to differentiate on
x = input("Enter a value x: ")

# if user input, attempt to make 'x' a float, else exit
if len(x) > 0:
    try:
        x = float(x)
    except:
        print("Bad input")
        garbage = input("Press <Enter> to end program")
        exit()
else:
    exit()

# try evaluating the function at x, if no good exit
try:
    garbage = f(x)
except:
    print("Bad function or f(x)")
    garbage = input("Press <Enter> to end program")
    exit()

# make variable h as small as possible float given what limitations computers can do with them
if abs(x) >= 1e+16 or (abs(x) <= 1e-16 and x != 0):
    digs, e = str(x).split('e')
    h = float("0.000000000000001e"+e)
else:
    left, right = str(x).split('.')
    h = 1
    for d in range(15-len(left)):
        h /= 10

# differentiate
y = (1/(2*h))*(f(x-2*h) - 4*f(x-h) + 3*f(x))

# ouput result
print("The differential of",function,"at x="+str(x),"is",y)
garbage = input("Press <Enter> to end program")
