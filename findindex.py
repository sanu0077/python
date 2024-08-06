# Function to find the index of the maximum value in an array
def find_max_index(array):
    max_value = max(array)
    max_index = array.index(max_value)
    return max_index

# Main code
def main():
    # Taking input for the size of the array
    size = int(input("Enter the size of the array: "))
    
    # Initializing an empty array
    array = []
    
    # Taking input for the array elements
    print("Enter the numbers:")
    for i in range(size):
        num = int(input(f"Element {i+1}: "))
        array.append(num)
    
    # Finding the index of the maximum value
    max_index = find_max_index(array)
    
    # Printing the result
    print(f"The index of the maximum value in the array is: {max_index}")

if __name__ == "__main__":
    main()
