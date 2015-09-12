#!/usr/bin/python

from progressbar import ProgressBar

trig = dict()
words = list()
new_ord = lambda x: ord(x)-96
triangulize = lambda word: sum(map(new_ord, word.lower()))

def main():
    with open('p042_words.txt') as f:
        words = f.read().replace('"','').split(',')

    sums = map(triangulize, words)
    sums_max = max(sums)

    global trig
    triangle = lambda n: n*(n+1)/2

    i = 1
    while True:
        trig[triangle(i)] = None
        if triangle(i) > sums_max:
            break
        i += 1

    progress = ProgressBar(maxval=len(words)).start()
    total = 0

    for i,w in enumerate(sums):
        if w in trig:
            total += 1
            print words[i]
        progress.update()

    progress.finish()
    print total


if __name__ == '__main__':
    main()