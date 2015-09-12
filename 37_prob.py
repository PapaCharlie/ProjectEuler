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
    def rotate(n):
        p,l,r = int(log(n,10)),n,n
        k = [n]
        for p in xrange(p,0,-1):
            l = l - (l/(10**p))*10**p
            r = r/10
            if l not in ls or r not in ls:
                return []
        return [n]
    ls = {key: None for key in rwh_primes1(n)}
    su = []
    for key in ls.keys():
        if key > 10:
            su += rotate(key)
    return su


if __name__ == '__main__':
    k =  main(1000000)
    print len(k),sum(k), k
