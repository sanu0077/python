my_list = [1, 2, 3, 4, 5]


# first_element = my_list[0]  # Access first element
# last_element = my_list[-1]  # Access last element

my_list.append(6)           # Add element to the end
my_list.insert(2, 2.5)      # Insert element at a specific position


for element in my_list:
    print(element)

squares = [x ** 2 for x in my_list]  # Create a new list with the squares of the elements

print(squares)