# Fractional Knapsack Problem

# Define a class to represent each item with weight and value
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate the maximum value for the Fractional Knapsack
def fractional_knapsack(capacity, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0  # Total value of items in the knapsack
    for item in items:
        if capacity > 0:
            if item.weight <= capacity:
                # If the item can be fully added
                total_value += item.value
                capacity -= item.weight
            else:
                # If only a fraction of the item can be added
                total_value += item.value * (capacity / item.weight)
                break  # Knapsack is full
    return total_value

# Example usage
items = [
    Item(value=60, weight=10),
    Item(value=100, weight=20),
    Item(value=120, weight=30)
]

capacity = 50
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in Knapsack = {max_value}")
