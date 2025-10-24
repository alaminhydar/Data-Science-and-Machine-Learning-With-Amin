"""
Functions in Python
==================
Functions are reusable blocks of code that perform a specific task.

Topics:
- Why use functions
- Built-in functions
- Defining your own functions
- Parameters vs Arguments
- Functions in ML
"""

# ---------------------------
# Importance in programming
# ---------------------------
# 1. Code reuse
# 2. Modularity
# 3. Easier debugging

# ---------------------------
# Built-in function example
# ---------------------------
print("Hello, world!")  # built-in print() function

# ---------------------------
# Defining your own function
# ---------------------------
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

print(greet("Amin"))

#Can reuse the same funstion with different value
print(greet("Hydar"))

# Function with multiple parameters
print('\n--- Function to Add Number ---')
def add_numbers(a, b):
    return a + b

print(add_numbers(10, 20))