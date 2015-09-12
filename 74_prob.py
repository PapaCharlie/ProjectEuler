#number63.py
#Paul Chesnais
#2013/06/30

"""This is a python module with purpose of solving project Euler 55th problem. The problem is the following:
    The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
    
    1! + 4! + 5! = 1 + 24 + 120 = 145
    
    Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
    
    169  363601  1454  169
    871  45361  871
    872  45362  872
    
    It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
    
    69  363600  1454  169  363601 ( 1454)
    78  45360  871  45361 ( 871)
    540  145 ( 145)
    
    Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
    
    How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?"""

from math import factorial

def factoop(n):
    l = [n]
    check = True
    su = 0
    while check:
        n = str(n)
        newSum = 0
        for x in range(0, len(n)):
            newSum += factorial(int(n[x]))
        try:
            i = l.index(newSum)
            l.append(newSum)
            check = False
            su += 1
        except ValueError:
            n = newSum
            l.append(newSum)
            su += 1
    return su

def code():
    total = 0
    for n in range(1,1000001):
        if n % 10000 == 0:
            print `n`
        if factoop(n) == 60:
            total += 1
    return total