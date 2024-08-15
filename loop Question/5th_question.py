# Q5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

string = str(input("Enter the string :"))
for char in string:
    if string.count(char) == 1:
        print(f"The first non-repeated character is {char}")
        break
    elif string.count(char) > 1 :
        print("No single character found")
        break