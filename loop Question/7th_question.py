# Q7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    n = int(input("Enter the value between 1 to 10 :"))
    if 1 <= n <= 10 :
        print("Thanks")
        break
    else:
        print("Invalid number try again")