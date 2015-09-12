#number63.py
#Paul Chesnais
#2013/06/30

"""This is a python module with purpose of solving project Euler 55th problem. The problem is the following:
    The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

    How many n-digit positive integers exist which are also an nth power?"""

def code():
    l = []
    numbers = 0
    for x in range(1,31):
        l.append(x)
    for j in l:
        for i in l:
            if len(str(i**j))==j:
                numbers += 1
    return numbers