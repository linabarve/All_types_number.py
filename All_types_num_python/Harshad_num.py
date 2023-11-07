			# Harshad Number...........
			
n = int(input("Enter the number:"))
a = n
s = 0

while n > 0:
    r = n % 10
    s = s + r
    n //= 10

if a % s == 0:
    print(f"{a} is a Harshad number.")
else:
    print(f"{a} is not a Harshad number.")


		

