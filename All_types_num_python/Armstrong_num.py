
	# Aarmstrong num three digit 153..............
	
import math	
n = int(input("Enter the number:"))
k = n
s = 0

while n > 0:
	r = n % 10
	j = r
	if j > 0:
		p = pow(j,3)
		s = s + p
		j = j // 10
	n = n // 10
	
if k == s:
	print("it is armstrong number:",s)
else:
	print("it is not armstrong number:",s) 
	


