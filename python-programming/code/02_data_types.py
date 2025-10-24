"""
Python Basics: Data Types
=========================
Core Python data types:
- int, float, str, bool
- list, tuple, dict, set

Topics covered:
- Type conversion
- Type checking
"""

print("""
    Python Basics: Data Types
    =========================
    Core Python data types:
    - int, float, str, bool
    - list, tuple, dict, set

    Topics covered:
    - Type conversion
    - Type checking
""")

# Integers and Floats
num1 = 10
num2 = 3.5

print('num 1 (is int): {}, num 2 (is float): {}\n'.format(num1, num2))

print("Sum(num 1 + num 2):", num1 + num2)
print("\nDivision:", num1 / num2)

# Strings
print('\n--- Strings ---')
text = "Crypto Trading"
print('Text to upper case: ',text.upper())
print('Text to lower case: ',text.lower())
print('Length of text: ',len(text))

# Booleans
print('\n--- Booleans(True | False)')
is_open = True
is_closed = False
print(is_open and is_closed)
print(is_open or is_closed)

# Type Conversion
print('\n--- Type Conversion ---')
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)
print(num_int, type(num_int))
print(num_float, type(num_float))
