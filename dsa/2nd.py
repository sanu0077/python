def find_max_index(arr):
    if len(arr) == 0:
        return None, None  # Return None if the list is empty
    
    max_value = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
            
    return max_value, max_index

# Input from user
array_size = int(input("Enter the size of the array: "))
arr = []
for i in range(array_size):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

max_value, max_index = find_max_index(arr)
print(f"The maximum value is {max_value} at index {max_index}")