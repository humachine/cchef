#http://www.codechef.com/JULY15/problems/EGBOBRD

import sys, math
T=raw_input()
for i in range(int(T)):
	tmp=raw_input()
	tmp=tmp.split()
	N,K=int(tmp[0]), int(tmp[1])

	tmp=raw_input()
	tmp=tmp.split()
	tmp=[int(x) for x in tmp]
	
	used=0
	for i in tmp:
		used=used+i
		flag=0
		if used%K!=0:
			flag=1
			used+=1
	if flag==1:
		used-=1
	print (used+K-1)/K	
