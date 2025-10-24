"""
Error Handling in Python
=======================
Python provides tools to handle errors gracefully.

Topics:
- Syntax, runtime, logical errors
- try, except, finally
- Importance in robust programs
"""
print(
    """
    Error Handling in Python
    =======================
    Python provides tools to handle errors gracefully.

    Topics:
    - Syntax, runtime, logical errors
    - try, except, finally
    - Importance in robust programs
"""
)
# ---------------------------
# Common Errors
# ---------------------------
# SyntaxError: print("Hello)
# RuntimeError: 10/0
# LogicalError: incorrect algorithm

# ---------------------------
# Handling errors
# ---------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("- Cannot divide by zero!")
finally:
    print("- Execution finished.")

# ---------------------------
# Why critical
# ---------------------------
# Prevents program crash
# Provides meaningful messages
# Enhances user experience
