# Function to print the first n terms of the Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Input from the user
n = int(input("Enter the number of terms: "))

# Get Fibonacci sequence
fib_sequence = fibonacci(n)

# Print the result
print(", ".join(map(str, fib_sequence)))
