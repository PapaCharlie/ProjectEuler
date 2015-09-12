#!/usr/bin/python

def code():
    p = [0]*1001
    for a in range(1001):
        for b in range(1001):
            for c in range(1001):
                square = a**2 + b**2
                s = a + b + c
                if s <= 1000:
                    if square == c**2:
                        p[s] += 1
    print max(enumerate(p), key = lambda x: x[1])

def main():
    dic = [0]*1000
    for p in xrange(3,1000):
        for a in xrange(1,p/2):
            for b in xrange(1,p/2-a+1):
                c = p - a - b
                a,b,c = a**2,b**2,c**2
                if (a+b+c) == 2*max(a,b,c):
                    dic[p] += 1
    print max(p.items, key=lambda x: x[1])

if __name__ == '__main__':
    code()