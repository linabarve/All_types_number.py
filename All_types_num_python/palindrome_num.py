 
		 # palindrome Number.............. 
n =  int(input())
k = n
s = 0
while n > 0:
	r = n % 10
	s = (s*10)+r
	n = n // 10
if s == k:
	print("It is palindrome  number:",s)
else:
	print("It is Not palindrome  number:",s)
