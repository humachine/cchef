#http://www.codechef.com/JULY15/problems/LCKYST

import sys, math
a=raw_input()
b=raw_input()
inp=b.split()
inp=[int(x) for x in inp]
precalc=[4, 744, 7744, 7744, 7744, 47744, 447744, 4447744, 44447744, 44447744, 74444447744, 74444447744, 474444447744, 4474444447744, 4474444447744, 4474444447744, 4474444447744]

for i in inp:
	p=1
	while i% (2**p) ==0:
		p+=1
	q=1
	while i% (5**q) ==0:
		q+=1
	if p>=q:
		print i
		continue
	print i* (4**((q-p+1)/2))

