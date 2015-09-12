#number34.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 34th problem. The problem is the following:
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

from math import factorial

def digify(n):
    """I hope I don't get sued for using this word"""
    string = str(n)
    l = []
    for x in range(0,len(string)):
        l.append(int(string[x]))
    return l

def factorialize(ls):
    if ls != list:
        l = digify(ls)
    else:
        l = ls[:]
    for x in range(0,len(l)):
        l[x] = factorial(l[x])
    return l

def code():
    total = 0
    for x in range(3,1000000):
        if sum(factorialize(x)) == x:
            total += x
    return total