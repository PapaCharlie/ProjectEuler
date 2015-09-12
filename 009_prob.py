#Paul Chesnais
#number9.py
#15/12/12
#!/usr/bin/python

"""This is a python module that answers this problem:

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

In answer to
Proect Euler's 9th problem"""

def code():
    for a in range(1000):
        for b in range(1000):
            for c in range(1000):
                if a < c and b < c:
                    square = a**2 + b**2
                    if square == c**2:
                        s = a + b + c
                        if s == 1000:

                            print "("+`a`+","+`b`+","+`c`+")"
                            return a*b*c

if __name__ == '__main__':
    code()