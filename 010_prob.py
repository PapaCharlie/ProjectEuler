#Paul Chesnais
#number9.py
#15/12/12

"""This is a python module that answers this problem:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

In answer to
Proect Euler's 10th problem"""

def isprime(n):
    b = 3
    while b < n:
        if n % b == 0:
            return False
        b += 1
    return True

def code():
    a = 1
    total = 0
    while a < 2000000:
        if isprime(a) == True:
            total += a
            print a
        a += 2
    return total + 2

#Hint, the answer, according to Mathematica, is 142913828922. Mathematica makes this too easy.