"""
Python Tuples
=============
Tuples are immutable sequences.

Topics:
- Creating tuples
- Accessing elements
- Immutability
- Why useful
"""

print("""
    Python Tuples
    =============
    Tuples are immutable sequences.

    Topics:
    - Creating tuples
    - Accessing elements
    - Immutability
    - Why useful
""")

# Creating tuples
coords = (10, 20)
colors = ("red", "green", "blue")

print('- ',coords)
print('- ',colors)
# Accessing
print("- X coordinate:", coords[0])
print("- First color:", colors[0])

# Immutability
# coords[0] = 15  # This would raise an error

# Using tuples in functions
print('\n--- Using tuples in functions ---')
def min_max(values):
    return min(values), max(values)

numbers = (3, 7, 16, 2, 9)
result = min_max(numbers)
print("- Min and Max:", result)
