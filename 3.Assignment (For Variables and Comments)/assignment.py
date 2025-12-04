"""
- You have $50
- You buy an item that is $15
- With a tax of 3%
- print how much money you have left
"""

# Soluton 1 (assigning to variables)
money = 50
item = 15
tax = item * 0.03
money_left = money - item - tax
print(money_left)

# Solution 2 (using the values directly)
print(50 - 15 - (15 * 0.03))
