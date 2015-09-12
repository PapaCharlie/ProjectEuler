from __future__ import division
from numpy import sqrt, inf

penta = lambda n: n*(3*n-1)/2

def is_penta(k):
    return (sqrt(24*k + 1)+1)/6 % 1 == 0

def generator():
    values = [penta(2),penta(1)]
    maxn = 2
    while True:
        for x in values[1:]:
            yield (values[0],x)
        maxn += 1
        values.insert(0, penta(maxn))

def main():
    mind = inf
    for m,n in generator():
        diff = abs(m-n)
        if is_penta(m+n) and is_penta(diff) and diff < mind:
            mind = diff
            print mind


if __name__ == '__main__':
    main()