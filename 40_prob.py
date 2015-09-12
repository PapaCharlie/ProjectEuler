#!/usr/bin/python

def main():
    s = ''.join(map(str,xrange(1,1000000)))
    print int(s[1-1]) , int(s[10-1]) , int(s[100-1]) , int(s[1000-1]) , int(s[10000-1]) , int(s[100000-1]) , int(s[1000000-1])
    return int(s[1-1]) * int(s[10-1]) * int(s[100-1]) * int(s[1000-1]) * int(s[10000-1]) * int(s[100000-1]) * int(s[1000000-1])

if __name__ == '__main__':
    print main()
