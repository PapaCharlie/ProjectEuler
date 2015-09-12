#!/usr/bin/python

def main():
    def check(n,d):
        n1,n2,d1,d2 = map(float,[n/10,n%10,d/10,d%10])
        if n1 == d1:
            return n2/d2 == n/float(d)
        elif n2 == d1:
            return n1/d2 == n/float(d)
        elif n1 == d2:
            return n2/d1 == n/float(d)
        elif n2 == d2:
            return n1/d1 == n/float(d)
        else:
            return False
    ls = []
    for n in [n for n in xrange(10,100) if n % 10 != 0]:
        for d in [d for d in xrange(int(n)+1,100) if d % 10 != 0]:
            if check(n,d):
                ls.append((n,d))
    for n,d in ls:
        print n,'/',d,'*',

if __name__ == '__main__':
    main()
