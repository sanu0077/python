# Q4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
# (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
fruit = str(input("Enter fruit name :"))
color = str(input("Enter the color of the fruit :"))
if color == "Green" :
    print(fruit,"is Unripe")
elif color == "Yellow" :
    print(fruit,"is Ripe")
else :
    print(fruit,"is Overripe")  