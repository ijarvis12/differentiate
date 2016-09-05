#!/usr/bin/python3

from math import *

print("")
print("This program finds the differential of a function using three-point derviative")
print("")

function = input("Enter a function f(x): ")

if len(function) == 0:
    exit()

f = lambda x: eval(function)

x = input("Enter a value x: ")

if len(x) > 0:
    try:
        x = float(x)
    except:
        print("Bad input")
        garbage = input("Press <Enter> to end program")
        exit()
else:
    exit()

try:
    garbage = f(x)
except:
    print("Bad function or f(x)")
    garbage = input("Press <Enter> to end program")
    exit()

if abs(x) >= 1e+16 or (abs(x) <= 1e-16 and x != 0):
    digs, e = str(x).split('e')
    h = float("0.000000000000001e"+e)
else:
    left, right = str(x).split('.')
    h = 1
    for d in range(15-len(left)):
        h /= 10

y = (1/(2*h))*(f(x-2*h) - 4*f(x-h) + 3*f(x))

print("The differential of",function,"at x="+str(x),"is",y)
garbage = input("Press <Enter> to end program")
