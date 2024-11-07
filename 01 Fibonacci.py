#  Fibonacci

# Recursive function to calculate Fibonacci numbers
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10
print(f"Fibonacci (Recursive) of {n}: {fibonacci_recursive(n)}")
'''
Time Complexity: O(2^n)
In the recursive method, each call splits into two more calls, creating a tree of exponential growth.
The function recalculates values multiple times, leading to inefficient time complexity.
'''

# Iterative function to calculate Fibonacci numbers
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage
n = 10
print(f"Fibonacci (Iterative) of {n}: {fibonacci_iterative(n)}")
'''
Time Complexity: O(n)
The iterative approach only requires a single loop, making it much faster than recursion.
It only needs n steps to calculate the n-th Fibonacci number without redundant calculations.
'''