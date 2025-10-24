"""
Python Basics: Variables
========================
Variables are containers for values.
They allow us to store, change, and retrieve data.

Topics covered:
- Assigning values
- Multiple assignments
- Variable types
- Updating values
"""

print("""
    Python Basics: Variables
    ========================
    Variables are containers for values.
    They allow us to store, change, and retrieve data.

    Topics covered:
    - Assigning values
    - Multiple assignments
    - Variable types
    - Updating values
""")

# ---------------------------
# Assigning Variables
# ---------------------------
age = 25          # integer
height = 1.75     # float
name = "Amin"     # string
is_data_scientist = True  # boolean

print('\n--- Assigned Variables ---')
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is c?", is_data_scientist)

# ---------------------------
# Multiple Assignment
# ---------------------------
print('\n--- Multiple Assignemnt ---')
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)

# ---------------------------
# Variable Types
# ---------------------------
print('\n--- Variable types ---')
print('Variable type of Age: {}'.format(type(age)))       # int
print('Variable type of Height: {}'.format(type(height)))    # float
print('Variable type of Name: {}'.format(type(name)))      # str
print('Variable type of Is Data Scientist: {}'.format(type(is_data_scientist))) # bool

# ---------------------------
# Updating Variables
# ---------------------------
print('\n--- Updating Variables ---')
age += 1
name = name.upper()
print("Updated age:", age)
print("Updated name:", name)
