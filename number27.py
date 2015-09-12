#!/usr/bin/python

def FastPrimeSieve(max):
    possible_primes =  range(3,max+1, 2)
    curr_index = -1
    max_index = len(possible_primes)
    for latest_prime in possible_primes:
        curr_index +=1
        if not latest_prime : continue
        for index_variable_not_named_j in xrange((curr_index+latest_prime),max_index, latest_prime): possible_primes[index_variable_not_named_j]=0
    possible_primes.insert(0,2)
    return [x for x in possible_primes if x > 0]

def main():
    def f(a,b,n):
        return n**2 + a*n + b
    primes = FastPrimeSieve(10000000)
    print "Got primes"
    m = 0,0,0
    for a in xrange(-1000,0):
        for b in xrange(-1000,0):
            n = 0
            while f(a,b,n) in primes:
                n += 1
            if m[0] < n:
                m = n,a,b
    print "Halfway there!"
    for a in xrange(1001):
        for b in xrange(1001):
            n = 0
            while f(a,b,n) in primes:
                n += 1
            if m[0] < n:
                m = n,a,b
    return m

if __name__ == '__main__':
    print main()