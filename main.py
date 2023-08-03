def addition(num1, num2):
    """Perform addition of two numbers. """
    return num1 + num2

def subtraction(num1, num2):
    """Perform subtraction of two numbers."""
    return num1 - num2

def multiplication(num1, num2):
    """Perform multiplication of two numbers."""
    return num1 * num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("The sum is:", addition(num1, num2))
print("The difference is:", subtraction(num1, num2))
print("The product is:", multiplication(num1, num2))
