# Function to print the Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=", " if i < n-1 else "\n")
        a, b = b, a + b

# Get user input
n = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
if n > 0:
    fibonacci(n)
else:
    print("Please enter a positive integer.")
