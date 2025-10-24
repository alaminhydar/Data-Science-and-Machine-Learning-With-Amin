"""
OOP Basics
==========
Object-Oriented Programming (OOP) is a programming paradigm using classes and objects.

Topics:
- Classes and objects
- Attributes & methods
- OOP in scalable AI systems
"""

# ---------------------------
# Defining a class
# ---------------------------
class Trader:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

# ---------------------------
# Creating an object
# ---------------------------
amin = Trader("Amin", 1000)

# Methods on the class
print(amin.name)
print(amin.deposit(500))
print(amin.withdraw(300))
