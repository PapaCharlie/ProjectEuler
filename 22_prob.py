#number22.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 22st problem. The problem is the following:
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
	3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
	So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?"""

def openNames():
    ls = []
    for line in open( "number22-names.txt", "r" ).readlines():
        for value in line.split('","'):
            ls.append( value )
    ls.sort()
    return ls

def order(s):
    return ord(s)-64

def summer(s):
    bleh = 0
    for x in range(0,len(s)):
        bleh += order(s[x])
    return bleh

def code():
    ls = openNames()
    total = 0
    for x in range(0,len(ls)):
        total += summer(ls[x])*(x+1)
    return total