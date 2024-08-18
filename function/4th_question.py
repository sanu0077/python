# Q4. Function Returning Multiple Values
# Problem: Create a function that returns both the
# area and circumference of a circle given its radius.


# import math

# def area(radius):
#     return math.pi * (radius ** 2)
# def circumferenece(radius):
#     return 2 * math.pi * radius

# print(area(9),circumferenece(9))



import math

def circle_stat(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

area, circumference = circle_stat(9)

# Print the values with 2 decimal places
print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")

