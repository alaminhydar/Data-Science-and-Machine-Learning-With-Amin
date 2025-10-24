"""
Python Lists
============
Lists are ordered collections of items.

Topics:
- Creating lists
- Indexing and slicing
- Adding/removing elements
- Iterating
"""

print("""
Python Lists
============
Lists are ordered collections of items.

Topics:
- Creating lists
- Indexing and slicing
- Adding/removing elements
- Iterating
""")

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Amin", 25, True]

print('--- Lists ---')
print('- ',fruits)
print('- ',numbers)
print('- ',mixed)

# Accessing elements
print('\n--- Accessing elements from list ---')
print("- First fruit:", fruits[0])
print("- Last number:", numbers[-1])

# Slicing
print("\n--- Slicing List ---")
print("- First two fruits:", fruits[:2])

# Adding elements
print('\n--- Appending to Lists ---')
fruits.append("orange")
fruits.insert(1, "mango")
print(fruits)

# Removing elements
print("\n--- Removing elements ---")
fruits.remove("banana")
popped = fruits.pop()
print('- ',fruits, "Popped:", popped)

# Iterating
print("\n--- Iterating List ---")
for fruit in fruits:
    print("- I like", fruit)
