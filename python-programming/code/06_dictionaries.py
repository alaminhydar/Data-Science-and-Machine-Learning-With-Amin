"""
Python Dictionaries
===================
Dictionaries store key-value pairs.

Topics:
- Creating dictionaries
- Accessing values
- Updating
- Iterating
"""

print("""
    Python Dictionaries
    ===================
    Dictionaries store key-value pairs.

    Topics:
    - Creating dictionaries
    - Accessing values
    - Updating
    - Iterating
""")

# Creating
student = {
    "name": "Amin",
    "age": 25,
    "courses": ["Python", "Trading"]
}

print('- ',student)
print('- ',student["name"])

# Updating
student["age"] = 26
student["email"] = "amin@example.com"

# Iterating
print('\n--- Iterating Student ---')
for key, value in student.items():
    print('- ',key, ":", value)
