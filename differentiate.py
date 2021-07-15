#!/usr/bin/python3

##                                                ##
## program differentiates a user inputed function ##
##                                                ##
from math import *
from decimal import Decimal, getcontext

print("")
print("This program finds the differential of a function using three-point derviative")
print("")

# set decimal objects precision
getcontext().prec = 16

# get function
function = input("Enter a function f(x): ")

# if no user input, exit
if len(function) == 0:
    exit()

# create function from input
f = lambda x: eval(function)

# get x value to differentiate on
x = input("Enter a value x: ")

# if user input, attempt to make 'x' a decimal object, else exit
if len(x) > 0:
    try:
        x = Decimal(x)
    except:
        print("Bad input")
        _ = input("Press <Enter> to end program")
        exit()
else:
    exit()

# try evaluating the function at x, if no good exit
try:
    _ = f(x)
except:
    print("Bad function or f(x)")
    _ = input("Press <Enter> to end program")
    exit()

# make step variable h as small as conveniently possible for eval(), uses floats
h = Decimal('0.000000000000001')

# differentiate
y = (Decimal(1)/(2*h))*Decimal(f(x-2*h) - 4*f(x-h) + 3*f(x))

# ouput result
print("The differential of",function,"at x="+str(x),"is",y)
_ = input("Press <Enter> to end program")
