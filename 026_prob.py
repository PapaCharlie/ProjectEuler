#number26
#Paul Chesnais
#2013-11-27


"""This is a python module with purpose of solving project Euler 17th problem. The problem is the following:
    A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10= 	0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
    
    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

def longDiv(n):
    #decs = []
    ls = []
    i = 1
    while True:
        d = i/n
        #decs.append(d)
        i = 10*(i - n*d)
        if i in ls and i != 0:
            ls.append(i)
            repeating = True
            break
        elif i == 0:
            ls.append(i)
            repeating = False
            break
        else:
            ls.append(i)
    if repeating:
        return len(ls) - (ls.index(ls[-1]) + 1)
    else:
        return 0

def code():
    ls = []
    for u in range(1,1000):
        if not (u%2 == 0 or u%5 == 0):
            ls.append(u)
    cycles = map(longDiv, ls)
    max = 0
    index = 0
    for u in range(len(cycles)):
        if cycles[u] > max:
            max = cycles[u]
            index = u
    return ls[index]