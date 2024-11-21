
    #------FIBONACCI RECURSIVE FUNCTION ------------------
def fibonacci_recursive(n):
    """Recursive function to return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10  # Change this to compute a different Fibonacci number
for i in range(n):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")


    #----------FIBONACCI  RECURSIVE DICTIONARY {} -------------
def fibonacci_with_dict(n, memo={}):
    """Fibonacci function using a dictionary for memoization."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    if n not in memo:
        memo[n] = fibonacci_with_dict(n - 1, memo) + fibonacci_with_dict(n - 2, memo)
    return memo[n]

# Example usage
n = 10  # Change this to compute a different Fibonacci number
for i in range(n):
    print(f"Fibonacci({i}) = {fibonacci_with_dict(i)}")
