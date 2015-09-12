#!/usr/bin/python

from math import log

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def main(n):
    def pan(n):
        s = str(n)
        for i in map(str,xrange(1,len(s)+1)):
            if i not in s:
                return False
        return True
    for n in rwh_primes1(n)[::-1]:
        if pan(n):
            return n
    return 0

if __name__ == '__main__':
    print main(100000000)
