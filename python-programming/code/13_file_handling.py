"""
File Handling
=============
Python can read/write files to store and retrieve persistent data.

Topics:
- Why it matters
- Open, read, write, append
- Real-world relevance
"""

print(
   """
    File Handling
    =============
    Python can read/write files to store and retrieve persistent data.

    Topics:
    - Why it matters
    - Open, read, write, append
    - Real-world relevance
""" 
)

# ---------------------------
# Writing to a file
# ---------------------------
with open("trades.txt", "w") as file:
    file.write("BTC: Buy 29000, Sell 29500\n")
    file.write("ETH: Buy 1800, Sell 1850\n")

# ---------------------------
# Reading from a file
# ---------------------------
with open("trades.txt", "r") as file:
    content = file.read()
    print(content)

# ---------------------------
# Appending to a file
# ---------------------------
with open("trades.txt", "a") as file:
    file.write("BNB: Buy 320, Sell 310\n")


with open("trades.txt", "r") as file:
    content = file.read()
    print(content)