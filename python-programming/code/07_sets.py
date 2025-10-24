"""
Python Sets
===========
Sets are unordered collections of unique items.

Topics:
- Creating sets
- Adding/removing elements
- Set operations
"""
print("""
    Python Sets
    ===========
    Sets are unordered collections of unique items.

    Topics:
    - Creating sets
    - Adding/removing elements
    - Set operations
""")

numbers = {1, 2, 3, 4, 4, 2}
print('- ',numbers)  # duplicates removed

# Add number 5 
numbers.add(5)

print('\n--- Remove number 2 ---')
numbers.remove(2)
print('- ',numbers)

# Set operations
print('\n--- Set opeartions ---')
a = {1, 2, 3}
b = {3, 4, 5}

print("- Union:", a | b)
print("- Intersection:", a & b)
print("- Difference:", a - b)
