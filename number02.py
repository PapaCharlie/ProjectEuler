#!/usr/bin/python

def main():
    a,b = 1,1
    s = 0
    while b < 4000000:
        a,b = b, a + b
        if b % 2 == 0:
            s += b
    print s

if __name__ == '__main__':
    main()