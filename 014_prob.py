#Paul Chesnais
#number14.py
#24/01/13

"""This is a python module that answers this problem:

The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

In answer to Proect Euler's 14th problem"""

def Collatz(n):
    if n % 2 == 0:
        n /= 2
        return n
    if n % 2 == 1:
        n = 3*n + 1
        return n

def chain(n):
    c = 1
    while n != 1:
        n = Collatz(n)
        c +=1
    return c

def code():
    n = 1
    maxchain = 0
    maxn = 0
    while n < 1000000:
        if chain(n) > maxchain:
            maxchain = chain(n)
            maxn = n
        n += 1
    print "Starting number: " + `maxn` + "\nChain length:" + `maxchain`





