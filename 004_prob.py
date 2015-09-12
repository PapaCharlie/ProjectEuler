#Paul Chesnais
#number4.py
#15/12/12

"""This is a python module that returns the highest palindrome that is a product of 2 3-digit numbers,
in answer to Proect Euler's 4th problem"""

def palcheck(s):
    """checks if s is a palindrome
    Precondition: s is a string"""
    if len(s) == 6:
        if s[0] == s[5]:
            if s[1] == s[4]:
                if s[2] == s[3]:
                    return True
    return False

def code():
    li = []
    for a in range(1000):
        for b in range(1000):
            m = a * b
            if palcheck(str(m)) == True:
                li.append(m)
            b -= 1
        b = 999
        a -= 1
    return max(li)

