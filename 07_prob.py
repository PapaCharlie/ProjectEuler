#Paul Chesnais
#number7.py
#15/12/12

"""This is a python module that returns the 10 001st prime number,
in answer to Proect Euler's 7th problem"""

def isprime(n):
    for b in range(2,n):
        if n % b == 0:
            return False

def code():
    a = 1
    n = 0
    while n != 10001:
        if isprime(a) != False:
            n +=1
        a += 2
    return a -2