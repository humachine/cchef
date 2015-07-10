#http://www.codechef.com/JULY15/problems/CHCUBE

import sys, math
a=raw_input()
for i in range(int(a)):
	b=raw_input()
	inp=b.split()
	
	x=inp[0]
	y=inp[1]

	if inp[2]==x or inp[3]==x:
		if inp[4]==x or inp[5]==x:
			print 'YES'
			continue
	
	if inp[2]==y or inp[3]==y:
		if inp[4]==y or inp[5]==y:
			print 'YES'
			continue
	print 'NO'
