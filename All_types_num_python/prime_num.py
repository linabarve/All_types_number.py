 
		  # Prime number................
	
n = int(input("enter the number:"))
c = 0

for i in range(1,n+1):
	if n % i == 0:
		c = c + 1
if c == 2:
	print("it is prime number:",i)
else:
	print("it is not prime number:",i)



			# prime number user input...........
		
n = int(input("Enter the number of numbers: "))

for _ in range(n):
    k = int(input())
    c = 0

    for i in range(1, k + 1):
        if k % i == 0:
            c = c + 1

    if c == 2:
        print("it is prime number:",i)
    else:
        print("it is Not prime number:",i)

  
