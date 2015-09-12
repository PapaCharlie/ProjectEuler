#!/usr/bin/python

from itertools import permutations

def main():
    ls = [2,3,5,7,11,13,17]
    def pan(n):
        s = ''.join(n)
        for i,n in enumerate(xrange(1,8)):
            if not int(s[n:n+3]) % ls[i] == 0:
                return False
        return True
    p = filter(pan,permutations(map(str,xrange(10))))
    return sum(map(lambda x:int(''.join(x)),p))

if __name__ == '__main__':
    print main()
