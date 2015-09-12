#!/usr/bin/python

from math import log

ls = {}

class yrange:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        global ls
        if len(ls) != 0:
            return ls.popitem()[0]
        else:
            raise StopIteration()

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def main(n):
    global ls
    ls = {key: None for key in rwh_primes1(n)}
    global su
    su = []
    def rotate(n):
        global ls
        global su
        p,t,gucci = int(log(n,10)),n,True
        k = [n]
        for _ in xrange(p):
            i = t%10
            t = i*10**p + t/10
            # print n,t,p
            if n != t:
                k.append(t)
                if gucci:
                    if not ls.has_key(t):
                        gucci = False
                elif ls.has_key(t):
                    del ls[t]
        if gucci:
            su += k
    for key in yrange():
        rotate(key)
    return su


if __name__ == '__main__':
    k =  main(1000000)
    print len(k),k
