import math

def permute(ints,n):
    if len(ints) == 0:
        return ''
    if len(ints) == 1:
        return `ints[0]`
    ints.sort()
    fac = math.factorial(len(ints)-1)
    i = (n/fac)
    n -= (i)*fac
    s = `ints.pop(i)`
    return s + permute(ints,n)

def code():
    return int(permute(range(10), 999999))
