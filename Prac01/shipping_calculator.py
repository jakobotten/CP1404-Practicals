"""
Program to calculate shipping cost for multiple items.
If the total cost is over $100.00, a 10% discount is applied to the total shipping cost.
"""

# Ask for initial number of items from user.
number_of_items = int(input("Number of items: "))

# Set the initial cost.
total_cost = 0.00

# Error checking: request another input if number_of_items value is negative.
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Ask the user for the price of each item.
for i in range(1, number_of_items + 1):
    print("Shipping cost of item", i, "is: ")
    cost_of_item = float(input("$"))
    total_cost += cost_of_item

# Apply 10% discount if total_cost is over $100
if total_cost > 100:
    total_cost -= total_cost / 10

# Output final cost to user.
print("Total cost for", number_of_items, "items is: $", total_cost)
