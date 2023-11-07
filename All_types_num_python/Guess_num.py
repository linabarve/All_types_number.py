        
         # Guess the number...............
	
n = int(input("Enter the number:"))
a = int(input("Enter the hidden number:"))
i = 1

while i <= n:
    k = int(input("Guess the number:"))

    if a == k:
        print("You win!")
        break
    elif a < k:
        print("Your guess is too high.")
    else:
        print("Your guess is too low")

    i = i + 1



