		  # Strong number................
		  
n = int(input("Enter the number:"))
a = n
s = 0

while n > 0:
    r = n % 10
    f = 1
    for j in range(1, r + 1):
        f *= j
    s += f
    n //= 10

if s == a:
    print("It is a strong number:", s)
else:
    print("It is not a strong number:", s)




			# strong number user input......
			
			
n = int(input("Enter the number of numbers: "))

for _ in range(n):
    k = int(input("Enter a number: "))
    a = k
    s = 0

    while k > 0:
        r = k % 10
        f = 1
        for i in range(1, r + 1):
            f *= i
        s += f
        k //= 10

    if s == a:
        print(f"{a} is a strong number.")
    else:
        print(f"{a} is not a strong number.")

