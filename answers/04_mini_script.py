"""ANSWER — Exercise 04"""
cart = [
    ("apples", 2.50),
    ("bread", 1.80),
    ("milk", 1.20),
]
total = 0.0
for item, price in cart:
    print(f"{item}: ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")
