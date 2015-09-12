#!/usr/bin/python

coins = [200, 100, 50, 20, 10, 5, 2, 1]

def generate(coins, total):
    if coins[0] == 1 or total == 0:
        return 1
    n = 0
    if coins[0] == total:
        n += 1
    if coins[0] + coins[0] == total:
        n += 1
    if coins[0] + coins[0] < total:
        n += generate(coins, total - coins[0])
    for t in range(len(coins) -1 ):
        if coins[0] + coins[t + 1] <= total:
            n += generate(coins[t + 1:], total - coins[0])
    return n

if __name__ == '__main__':
    n = 0
    for t in range(len(coins)):
        n += generate(coins[t:], 200)
    print n