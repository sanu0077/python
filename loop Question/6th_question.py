# Q6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

n = int(input("Enter the number that you wants to get factorial value :"))
factorial = 1
while n > 0 :
    factorial = factorial * n
    n = n - 1
    print(factorial)  # to check or print every step
print(factorial)    