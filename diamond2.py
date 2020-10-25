n = 10
n = 2 * n + 1
for i in range(n):
	for j in range(n):
		if ( i+j >= n//2 and i-j <= n//2
				and i+j+2 <= n+n-n//2 and j-i <= n//2):
			print("*",end="")
		else:
			print(" ",end="")
	print("")