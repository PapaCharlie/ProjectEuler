#number21.py
#Paul Chesnais
#2013/03/27

"""This is a python module with purpose of solving project Euler 21st problem. The problem is the following: 
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def  properDivisorsSum(n):
	div = []
	for x in range(1,n):
		if n % x == 0:
			div.append(x)
	return sum(div)

def checker(n):
	k = properDivisorsSum(n)
	if (n == properDivisorsSum(k) and n != k):
		return True
	else:
		return False

def code():
	ls = []
	count = 2
	while count != 10000:
		ls.append(count)
		count +=1
	amicableSum = 0
	i = 0
	while len(ls) != 0:
		n = ls.pop(0)
		if checker(n):
			amicableSum += n
			amicableSum += ls.pop(ls.index(properDivisorsSum(n)))
	print amicableSum

if __name__ in ('__main__', '__android__'):
    YourApp().run()