# Q8. Prime Number Checker
# Problem: Check if a number is prime.

prime = int(input("Enter thevalue that you wants to check :"))
is_prime = True

if prime > 1:
    for i in range(2,prime):
        if prime % i == 0:
            is_prime = False
            break
print(is_prime)        