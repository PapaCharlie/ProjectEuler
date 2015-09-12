#number19.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 19th problem. The problem is the following:
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

def monthDays(month,boop=False):
    if month == 2:
        if boop:
            return 29
        return 28
    elif month == 1 or month == 3 or month == 5  or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30

def isLeap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            return False
        return True
    return False

def plusSunday(date):
    days = monthDays(date[1],isLeap(date[2]))
    date[0] += 7
    if date[0] > days:
        date[1] += 1
        date[0] -= days
    if date[1] == 13:
        date[1] = 1
        date[2] += 1

def code():
    firstSunday = [6,1,1901]
    counter = 0
    while firstSunday[2] < 2001:
        plusSunday(firstSunday)
        if firstSunday[0] == 1:
            counter += 1
    print firstSunday
    return counter