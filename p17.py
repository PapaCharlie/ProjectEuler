a = len('hundredand')*99*9 #the hundreds
b = len('onetwothreefourfivesixseveneightnine')*190 # naughts, 20-90, the hundreds, 
c = len('teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen')*10 # one for each hundred
d = len('twentythirtyfortyfiftysixtyseventyeightyninety')*100 
print a + b + c + d  + len('onethousand') + len('hundred')*9


def sumnumb(n):
    result = 0
    for i in range(1,n+1):
        result = result + anglicize(i)
        
    return result
            
def anglicize(n):
    """Returns: English equivalent of n.
    
    Examples:
        3:      "three"
        45:     "forty five"
        100:    "one hundred"
        127:    "one hunded twenty seven"
        1001:   "one thousand one"
        999099: "nine hundred ninety thousand ninety nine
    
    Precondition: 0 < n < 1,000,000"""
    
    # Enforce precondition
    
    # Carry out rest of code
    if n < 1000:
        return anglicize1000(n)
    
    # n >= 1000
    # conditional expression to get number 1...999
    suffix = 0 if n % 1000 == 0 else anglicize1000(n % 1000)
    return (anglicize1000(n/1000) + len('thousand')+ suffix)


def anglicize1000(n):
    """Yields: English equiv of n.
    
    Precondition: n in 1..999"""
    # Enforce precondition
    
    # Carry out rest of code
    if n < 20:
        return anglicize1to19(n)
    
    # n >= 20
    if n < 100:
        return anglicize20to99(n)
    
    # n >= 100
    return anglicize100to999(n)


def anglicize1to19(n):
    """Returns: English equiv of n.
    
    Precondition: n in 1..19"""
    # Enforce precondition
    
    # Carry out rest of code
    if n == 1:
        return len('one')
    elif n == 2:
        return len('two')
    elif n == 3:
        return len('three')
    elif n == 4:
        return len('four')
    elif n == 5:
        return len('five')
    elif n == 6:
        return len('six')
    elif n == 7:
        return len('seven')
    elif n == 8:
        return len('eight')
    elif n == 9:
        return len('nine')
    elif n == 10:
        return len('ten')
    elif n == 11:
        return len('eleven')
    elif n == 12:
        return len('twelve')
    elif n == 13:
        return len('thirteen')
    elif n == 14:
        return len('fourteen')
    elif n == 15:
        return len('fifteen')
    elif n == 16:
        return len('sixteen')
    elif n == 17:
        return len('seventeen')
    elif n == 18:
        return len('eighteen')
    
    # n = 19
    return len('nineteen')


def anglicize20to99(n):
    """Returns: English equiv of n.
    
    Precondition: n in 20..99"""
    # Enforce precondition
    
    # Carry out rest of code
    return tens(n/10) + (0 if n % 10 == 0 else anglicize1to19(n % 10))


def anglicize100to999(n):
    """Returns: English equiv of n.
    
    Precondition: n in 100..999"""
    # Enforce precondition
    assert type(n) == int, 'Value '+str(n)+' is not an int'
    assert 99 < n and n < 1000, 'Value '+str(n)+' is not in the range 100..999'

    # Carry out rest of code
    # Anglicize the first three digits
    hundreds = n % 100
    suffix = 0
    if hundreds > 0 and hundreds < 20:
        suffix = anglicize1to19(hundreds)
    elif hundreds > 20:
        suffix = anglicize20to99(hundreds)
    if n% 100>0:
        return anglicize1to19(n/100) + len('hundredand') + suffix
    return anglicize1to19(n/100) + len('hundred') + suffix


def tens(n):
    """Returns: tens-word for n
    
    Precondition: n in 2..9"""
    # Enforce precondition
    assert type(n) == int, 'Value '+str(n)+' is not an int'
    assert 1 < n and n < 10, 'Value '+str(n)+' is not in the range 2..9'

    # Carry out rest of code
    if n == 2:
        return len('twenty')
    elif n == 3:
        return len('thirty')
    elif n == 4:
        return len('forty')
    elif n == 5:
        return len('fifty')
    elif n == 6:
        return len('sixty')
    elif n == 7:
        return len('seventy')
    elif n == 8:
        return len('eighty')
    
    return len('ninety')
