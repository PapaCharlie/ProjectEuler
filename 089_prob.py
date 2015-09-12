#number89.py
#Paul Chesnais
#2013/04/01

"""This is a python module with purpose of solving project Euler 89th problem. The problem is the following:
    The rules for writing Roman numerals allow for many ways of writing each number (see About Roman
    Numerals...). However, there is always a "best" way of writing a particular number.
    
    For example, the following represent all of the legitimate ways of writing the number sixteen:
    
        IIIIIIIIIIIIIIII
        VIIIIIIIIIII
        VVIIIIII
        XIIIIII
        VVVI
        XVI
    
    The last example being considered the most efficient, as it uses the least number of numerals.
    
    The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers
    written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending
    units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this
    problem).
    
    Find the number of characters saved by writing each of these in their minimal form.
    
    Note: You can assume that all the Roman numerals in the file contain no more than four consecutive
    identical units."""

letters = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
values = [1000, 500, 100, 50, 10, 5, 1]

def openNumerals():
    ls = open( "number89-numerals.txt", "r" ).readlines()
    for x in range(0,len(ls)-1):
        ls[x] = ls[x][:-1]
    return ls

def contracter(s):
    """Returns the length of the longest chain, the starting index, and the letter"""
    index = 0
    chain = 1
    status = True
    current = ''
    beep = 0
    l=[[],[]]
    while status:
        try:
            int(s[0])
            break
        except ValueError:
            pass
        current = s[index]
        if s[index+1] == current:
            chain += 1
        else:
            s = s[chain:] + `chain`+current
            l[1].append(chain)
            chain = 1
            index = -1
        index += 1
    l[0] = s
    return l

def economise(bleh):
    s = bleh
    index = 0
    letter = 0
    length = 0
    current = ""
    while index != len(s):
        current = s[index]
        if not index == len(s) -1 and s[index+1] == current:
            length += 1
            if length == 5 and current != 'M' and (letters.index(current)%2 == 0 or current == 'I'):
                s = s[0:s.find(current)] +letters[letters.index(current)-1]+ s[index+1:]
                index -= 4
                length = 0
            elif length == 2 and current != 'M' and current != 'I' and letters.index(current)%2 != 0:
                s = s[0:s.find(current)] +letters[letters.index(current)-1]+ s[index+1:]
                index -= 2
                length = 0
        index += 1
    if len(bleh) == len(s):
        return bleh
    return economise(s)
