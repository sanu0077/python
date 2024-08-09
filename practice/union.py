# Define sets
set1 = {1, 2, 3, 4}
set2 = {1, 3}

# Intersection
intersection = set1 & set2
print("Intersection:", intersection)  # Output: {1, 3}

# Union
union = set1 | set2
print("Union:", union)  # Output: {1, 2, 3, 4}

# Difference (elements in set1 but not in set2)
difference = set1 - set2
print("Difference (set1 - set2):", difference)  # Output: {2, 4}

# Difference (elements in set2 but not in set1)
difference2 = set2 - set1
print("Difference (set2 - set1):", difference2)  # Output: set()

# Symmetric Difference (elements in either set1 or set2 but not both)
symmetric_difference = set1 ^ set2
print("Symmetric Difference:", symmetric_difference)  # Output: {2, 4}

# Checking subset
is_subset = set2 <= set1
print("Is set2 a subset of set1?:", is_subset)  # Output: True

# Checking superset
is_superset = set1 >= set2
print("Is set1 a superset of set2?:", is_superset)  # Output: True

# Add an element to set1
set1.add(5)
print("Set1 after adding 5:", set1)  # Output: {1, 2, 3, 4, 5}

# Remove an element from set1
set1.remove(5)
print("Set1 after removing 5:", set1)  # Output: {1, 2, 3, 4}
