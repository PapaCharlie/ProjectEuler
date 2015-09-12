#!/usr/bin/python
#Paul Chesnais
#number15.py
#24/01/13

"""This is a python module that answers this problem:

Starting in the top left corner of a 2 by 2 grid, there are 6 routes (without backtracking) to the bottom
right corner.

How many routes are there through a 20 by 20 grid?

In answer to Proect Euler's 15th problem"""

from math import log,floor
import sys

bleh = [111,1011,1101,1110,10011,10101,10110,11001,11010,11100,100011,100101,100110,101001,101010,101100,110001,110010,110100,111000]

def binarizer(n,boo):
    """ This returns n in binary form (base 2) as a string if boo == true, else returns number of ones in
        the string
        Eg: 27,true -> '11011'
        Eg: 27,false -> 4"""

    s = ""

    if n == 1.0:
        s += "1"
        return s
    if n == 0.0:
        s += "0"
        return s
    while n > 1:
        s += "1"
        p = floor(log(n,2))
        if 2**p == n:
            zeros = p
        else:
            zeros = p -floor(log(n - 2**p,2))
        while zeros != 1:
            s += "0"
            zeros -= 1
        n -= 2**p
        if n == 1.0:
            s += "1"
        if n == 0.0:
            s += "0"
    if boo:
        return s
    else:
        return s.count("1")

def debine(s):
    """This function "debinarizes" binarized numbers made by the binarizer function
        Eg: "11011" -> 27"""
    power = 0
    num = 0
    index = -1
    while len(s) != (-1*(index+1)):
        if s[index] == "1":
            num += 2**(-1*(index + 1))
        index -= 1
    return num

def listBleh(l):
    ls = []
    for x in range(1,20):
        ls.append(debine(`l[x-1]`))
    ls.sort()
    count = 0
    ls2 = []
    while count != 19:
        ls2.append(binarizer(ls[count],True))
        count += 1

    count = 0
    boop = False
    while count != 19:
        boop = (int(ls2[count]) == l[count])
        print `ls2[count]`+ "        "+ `l[count]` + "    " + `boop`
        count += 1

def swapMany(l,i1,i2,i3,i4):
    boop = l[i1:i2]
    l[i1:i2] = l[i3:i4]
    l[i3:i4] = boop

def swap(l,i):
    """Swaps l[i] with l[i-1]"""
    boop = l[i]
    l[i] = l[i-1]
    l[i-1] = boop


def checker(l,h=20,w=20):
    for x in range(0,w):
        if l[x] != 1:
            return False
    for x in range(w,w+h):
        if l[x] != 0:
            return False
    return True

def latticer(h=20,w=20):
    l = []
    for x in range(1,h+1):
        l.append(0)
    for x in range(1,w+1):
        l.append(1)
    return l

def leftmost(l,boop=True):
    """Returns index of first 1 after leftmost chain of 0's in l if boop, else returns index of first zero
        Eg: True:  [1,1,0,0,1,0,0,0,1]-> 4
            False: [1,1,0,0,1,0,0,0,1]-> 2"""
    index = l.index(0)
    while l[index]== 0:
        index += 1

    if boop:
        return index
    else:
        return l.index(0)

def swapper(l):
    """Swaps last 0 of leftmost chain with next index (hint: it's a 1) and puts all remaining zeros back at the begining
        Eg: [1,1,0,0,1,0,0,0,1] -> [0,1,1,1,0,0,0,0,1]"""

    try:
        leftmost(l)
    except IndexError:
        return False

    if (leftmost(l) - leftmost(l,False)) == 1:
        swap(l,leftmost(l))
    else:
        swap(l,leftmost(l))
        swapMany(l,leftmost(l,False),leftmost(l),0,leftmost(l,False))
    return True

def inverter(l):
    ls = l[:]
    for x in range(0,len(ls)):
        ls[x] = (ls[x]-1)*-1
    return ls

def code(length=20):
    """code() is now officially replaced with fakeCode(). Deal with it. Edit: Just kidding... code() will
        now make judicous use of fakeCode(). I love you fakeCode(). You are the answer to all my problems.
        Enough bull. This finds all the lattice paths in square grid of side length length"""

    cornPos = [1,length -1]
    count = 2
    while cornPos[0] != length:
        count += (fakeCode(cornPos[0],cornPos[1]))**2
        cornPos[0] += 1
        cornPos[1] -= 1
    return count

def fakeCode(height=20,width=20):
    """This answers the problem for the 20*20 grid by default, else for grid of height height and width
        width. Edit: this will be used as core function of code(). Finds number of lattice paths without
        backtracking in grid of width*height"""
    if height == width:
        return code(height)
    l = latticer(height,width)
    count = 1
    boop = swapper(l)
    while boop:
        boop = swapper(l)
        count += 1
    return count

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print code(int(sys.argv[1]))
    else:
        print code()