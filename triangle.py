import math
a=int(input("Edge 1: "))
b=int(input("Edge 2: "))
c=int(input("Edge 3: "))
p=(a+b+c)/2
p=p*(p-a)*(p-b)*(p-c)
if p <= 0:
	print("Oops! Not a triangle.")
else:
	print("Area is:",math.sqrt(p))