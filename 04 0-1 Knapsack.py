# Function to solve the 0-1 Knapsack problem using Dynamic Programming
def knapsack_01(capacity, weights, values, n):
    # Initialize a DP table with 0s
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Max of including or not including the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Cannot include the item if it's heavier than the current capacity
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
max_value = knapsack_01(capacity, weights, values, n)
print(f"Maximum value in Knapsack = {max_value}")
