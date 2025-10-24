"""
Pythonic Concepts
=================
Advanced Python features that allow concise, readable, and efficient code.

Topics:
- List comprehensions
- Lambda functions
- Map, filter, reduce
- Generators and iterators
"""

print(
    """
    Pythonic Concepts
    =================
    Advanced Python features that allow concise, readable, and efficient code.

    Topics:
    - List comprehensions
    - Lambda functions
    - Map, filter, reduce
    - Generators and iterators
    """  
)

# List comprehension
print('--- List Comprehension ---')
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)

# Lambda
print('\n--- Lambda function ---')
add = lambda x, y: x + y
print(add(10, 20))

# Map, Filter, Reduce
from functools import reduce
nums = [1, 2, 3, 4, 5]
print('\nNums:', nums)
print('\n--- Using map function ---')
print('- ',list(map(lambda x: x*2, nums)))

print('\n--- Using filter function ---')
print('- ',list(filter(lambda x: x%2==0, nums)))

print('\n--- Using reduce function ---')
print('- ',reduce(lambda x, y: x+y, nums))

# Generator
print('\n --- Using a Generator function ---',)
def gen_numbers(n):
    for i in range(n):
        yield i

for val in gen_numbers(5):
    print(val)
