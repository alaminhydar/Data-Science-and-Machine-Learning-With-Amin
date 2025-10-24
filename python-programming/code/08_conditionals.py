"""
Python Conditionals
==================
Control program flow with if, elif, else.
"""


print("""
    Python Conditionals
    ==================
    Control program flow with if, elif, else.
""")

x = 10

if x > 0:
    print("- Positive")
elif x == 0:
    print("- Zero")
else:
    print("- Negative")

# Nested conditions
score = 85
if score >= 90:
    print("- A")
elif score >= 80:
    print("- B")
else:
    print("- C")
