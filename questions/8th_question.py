# Q8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = str(input("Enter the password :"))
if len(password) < 6 :
    print("weak")
elif len(password) < 11:
    print("medium")
else:
    print("Strong")    