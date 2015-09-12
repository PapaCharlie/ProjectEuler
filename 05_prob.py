#Paul Chesnais
#number5.py
#15/12/12

"""This is a python module that returns the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20, in answer to Proect Euler's 5th problem"""

def checker10(a):
    c = 0
    for b in range(1,11):
        if a % b != 0:
            return False

def code10():
    a = 1
    while checker10(a) == False:
        a += 1
    return a

def checker20(a):
    for b in range(1,21):
        if a % b != 0:
            return False

def code20():
    a = 1
    while checker20(a) == False:
        a += 1
    return a
