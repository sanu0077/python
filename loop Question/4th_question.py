# Q. 4. Reverse a String
# Problem: Reverse a string using a loop.

string = str(input("Enter th estring that you wants to reverse :"))
rev_string = ""
for char in string:
    rev_string = char + rev_string
print(rev_string)    