#Paul Chesnais
#number6.py
#15/12/12

"""This is a python module that returns the difference between the sum
of the squares of the first one hundred natural numbers and the square
of the sum, in answer to Proect Euler's 6th problem"""

def code():
    a = 0
    total1 = 0
    while a < 100:
        a += 1
        total1 += a
    total1 = total1 * total1
    a = 0
    total2 = 0
    while a < 100:
        a += 1
        total2 += a**2
    final = total1 - total2
    return final

if __name__ in ('__main__', '__android__'):
    number6().run()