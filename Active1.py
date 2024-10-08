# Function to perform multiplication
def multiply(num1, num2):
    # Return the product of the two numbers
    return num1 * num2

# Main program
if __name__ == "__main__":
    # Input: getting numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Call the function and store the result
    result = multiply(num1, num2)
    
    # Output: Display the result
    print(f"The result of multiplying {num1} and {num2} is: {result}")

                