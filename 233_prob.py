#number89.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 89th problem. The problem is the following:
    Let f(N) be the number of points with integer coordinates that are on a circle passing through (0,0), (N,0),(0,N), and (N,N).

It can be shown that f(10000)=36.

What is the sum of all positive integers N<=10^11 such that f(N)=420?"""

from math import sqrt

def circle(x,t):
    c = sqrt(t**2 + 4*t*x - 4*x**2)
    return [-(c - t)/2.0, (c + t)/2.0]

def integers(t):
    count = 0
    for i in range(int(t/2.0 - t/sqrt(2)), t/2 + 1):
        count += checkInt(i,t)
    count *= 2
    if t%2 == 0:
        count -= checkInt(t/2,t)
    return count

def checkInt(i,t):
    count = 0
    c = circle(i,t)
    if c[0]%1 == 0:
        count += 1
    if c[1]%1 == 0:
        count += 1
    return count

def code():
    x = 10000
    total = 0
    while x <= 10**11:
        if integers(x) == 420:
            total += x
            print x
        if x % 100000 == 0:
            print x
        x += 1
