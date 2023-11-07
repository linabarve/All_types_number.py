
		# composit number...............
		# Having   factor more than two..........

n = int(input("Enter the number:"))
c = 0

for i in range(1, n + 1):
    if n % i == 0:
        c = c + 1

if c > 2:
    print("It is a composite number. It has", c, "factors.")
else:
    print("It is not a composite number. It has", c, "factors.")

	

		
		
		# composite user numbere..............
		
n = int(input("Enter the number of numbers: "))

for _ in range(n):
    k = int(input())
    c = 0

    for i in range(1, k + 1):
        if k % i == 0:
            c = c + 1

    if c > 2:
        print(f"{num} is a composite number. It has {c} factors.")
    else:
        print(f"{num} is not a composite number. It has {c} factors.")

