

		# Happy Number & Sad Number...............
	
n = int(input())
s =  0
while n > 0:
	r = n%10
	s = s + r * r
	n = n // 10
if s == 1:
	print("Happy number:",n)
elif s == m:
	print("sad numbber:",n)
