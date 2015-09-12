#!/usr/bin/python

from itertools import permutations

pans = dict()

def test(num):
    def make(k): return sum([i*10**(n) for n,i in enumerate(reversed(k))])
    for m in range(1,7):
        for e in range(m + 1,9):
            multiplicand = make(num[0:m])
            multiplier = make(num[m:e])
            product = make(num[e:])
            # print multiplicand, multiplier, product
            if multiplicand < multiplier and multiplicand * multiplier == product and (min(multiplier, multiplicand),max(multiplier, multiplicand)) not in pans:
                pans[(min(multiplier, multiplicand),max(multiplier, multiplicand))] = product
                return product
    return 0

def main():
    for num in permutations([1,2,3,4,5,6,7,8,9],9):
        test(num)
    return sum(set(pans.values()))

if __name__ == '__main__':
    print main()
    # test(range(1,10))
    # print test([3,9,1,8,6,7,2,5,4])