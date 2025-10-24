"""
Full Python Example: Mini Crypto Trade Journal
===============================================
Combines variables, lists, dictionaries, conditionals, and loops
"""
print("""
    Full Python Example: Mini Crypto Trade Journal
    ===============================================
    Combines variables, lists, dictionaries, conditionals, and loops
""")

# Sample trades
trades = [
    {"coin": "BTC", "entry": 29000, "exit": 29500},
    {"coin": "ETH", "entry": 1800, "exit": 1850},
    {"coin": "BNB", "entry": 320, "exit": 310},
]

# Calculate profit/loss
for trade in trades:
    entry = trade["entry"]
    exit_price = trade["exit"]
    profit = exit_price - entry
    trade["profit"] = profit
    status = "Profit" if profit > 0 else "Loss"
    print(f"- {trade['coin']} trade: {status} of ${profit}")

# Summary
total_profit = sum([t["profit"] for t in trades])
print("- Total P/L:", total_profit)
