n = 1000

from math import sqrt

for i in range(2,n+1):
	isprime = True
	for j in range(2,int(sqrt(i))+1):
		if not i%j:
			isprime = False
			break
	if isprime:
		print (i,end="\t")
