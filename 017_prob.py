#number17.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 17th problem. The problem is the following:
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
    3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters
    would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
    and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in
    compliance with British usage."""

def belowTen(n):
    if n == 9:
        return "nine"
    if n == 8:
        return "eight"
    if n == 7:
        return "seven"
    if n == 6:
        return "six"
    if n == 5:
        return "five"
    if n == 4:
        return "four"
    if n == 3:
        return "three"
    if n == 2:
        return "two"
    if n == 1:
        return "one"
    if n == 0:
        return ""

def tweens(n):
    if n == 19:
        return "nineteen"
    if n == 18:
        return "eighteen"
    if n == 17:
        return "seventeen"
    if n == 16:
        return "sixteen"
    if n == 15:
        return "fifteen"
    if n == 14:
        return "fourteen"
    if n == 13:
        return "thirteen"
    if n == 12:
        return "twelve"
    if n == 11:
        return "eleven"
    if n == 10:
        return "ten"
    if n < 10:
        return belowTen(n)

def tents(n):
    units = n%10
    tens = n - units
    if tens == 90:
        return "ninety" + belowTen(units)
    if tens == 80:
        return "eighty" + belowTen(units)
    if tens == 70:
        return "seventy" + belowTen(units)
    if tens == 60:
        return "sixty"  + belowTen(units)
    if tens == 50:
        return "fifty" + belowTen(units)
    if tens == 40:
        return "forty" + belowTen(units)
    if tens == 30:
        return "thirty" + belowTen(units)
    if tens == 20:
        return "twenty" + belowTen(units)
    if tens == 10:
        return tweens(n)
    if tens == 0:
        return belowTen(n)

def hundreds(n):
    tens = n%100
    hundreds = n - tens
    hundreds /= 100
    if tens == 0:
        return belowTen(hundreds) + "hundred"
    return  belowTen(hundreds) + "hundredand" + tents(tens)

def spell(n):
    if n < 10:
        return belowTen(n)
    if n < 100:
        return tents(n)
    if n >= 100:
        return hundreds(n)

def code():
    s = ''
    for x in range(1,1000):
        s += spell(x).strip()
    s += "onethousand"
    return len(s)
