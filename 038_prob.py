pans = set(range(1,10))

def test(k):
    def make(k): return sum([i*10**(n) for n,i in enumerate(reversed(k))])
    def split(m):
        ls = list()
        while m != 0:
            ls.insert(0,m%10)
            m /= 10
        return ls
    ls = list()
    n = 1
    while True:
        ls += split(k*n) # len(ls) increases at every iteration, this loop must terminate
        if len(ls) > 9:
            return None
        if set(ls) == pans:
            return make(ls)
        n += 1

def main():
    max_k = 0
    max_n = 0
    for n in range(1,100000):
        k = test(n)
        if k > max_k:
            max_k = k
            max_n = n
    return max_n, max_k

if __name__ == '__main__':
    print main()
