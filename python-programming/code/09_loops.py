"""
Python Loops
============
Loops allow repetition.

Types:
- for loop
- while loop
"""

print("""
    Python Loops
    ============
    Loops allow repetition.

    Types:
    - for loop
    - while loop
""")

# For loop over list
fruits = ["apple", "banana", "cherry"]
print(fruits)
for fruit in fruits:
    print('- ',fruit)

print('\n')
# For loop with range
for i in range(5):
    print("- Number:", i)

print('\n --- While loop ---')
# While loop
count = 0
while count < 5:
    print("Counting:", count)
    count += 1

print('\n ---Nested loop ---')
# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)
