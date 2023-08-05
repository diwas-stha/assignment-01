def addition(num1, num2):
    """Perform addition of two numbers."""
    return num1 + num2


def subtraction(num1, num2):
    """Perform subtraction of two numbers."""
    return num1 - num2


def multiplication(num1, num2):
    """Perform multiplication of two numbers."""
    return num1 * num2


def division(num1, num2):
    """Perform division of two numbers."""
    if num2 == 0:
        print("Division by zero is not allowed!")
    return num1 / num2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("The sum is:", addition(num1, num2))
print("The difference is:", subtraction(num1, num2))
print("The product is:", multiplication(num1, num2))
print("The quotient is:", division(num1, num2))
