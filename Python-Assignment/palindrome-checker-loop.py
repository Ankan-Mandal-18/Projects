def is_palindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()
    
    # Initialize a variable to hold the reversed string
    reversed_string = ""
    
    # Loop through the original string in reverse order
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    
    # Check if the original string is the same as the reversed string
    return string == reversed_string

# Example usage
input_string = "madam"
output = is_palindrome(input_string)
print(output)  # Output: True
