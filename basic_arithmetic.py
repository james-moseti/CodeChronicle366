def add(num1, num2, num3=''):
    """A function to add two numbers passed"""
    if num3:
        return num1 + num2 + int(num3)
    else:
        return num1 + num2

def subtract(num1, num2):
    """function to get the difference between the passed two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """function to get the product of the passed numbers"""
    return num1 * num2

def divide(num1, num2):
    """function to get the quotient of the passed numbers"""
    if num2 == 0:
        print("Cannot divide a number by zero")
    else:
        return num1 / num2
    
def floor_divide(num1, num2):
    """function to perform floor division"""
    if num2 == 0:
        print("Cannot divide a number by zero")
    else:
        return num1 // num2
    
def modulus(num1, num2):
    """function to get the reminder of the division of the passed two numbers"""
    if num2 == 0:
        print("Cannot divide a number by zero")
    else:
        return num1 % num2


# addition
print("ADDITION")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
sum = add(firstNumber, secondNumber)
print(f"The sum of {firstNumber} and {secondNumber} is: {sum}")

# subtraction
print("\nSUBTRACTION")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
difference = subtract(firstNumber, secondNumber)
print(f"The difference between {firstNumber} and {secondNumber} is: {difference}")

# multiplication
print("\nMULTIPLICATION")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
product = multiply(firstNumber, secondNumber)
print(f"The product of {firstNumber} and {secondNumber} is: {product}")

# division
print("\nDIVISION")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
quotient = divide(firstNumber, secondNumber)
print(f"The result of dividing  {firstNumber} by {secondNumber} is: {quotient}")

# floor division
print("\nFLOOR DIVISION")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
fQuotient = floor_divide(firstNumber, secondNumber)
print(f"The result of floor division of {firstNumber} by {secondNumber} is: {fQuotient}")

# modulus
print("\nMODULUS")
firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("enter the second number: "))
remainder = modulus(firstNumber, secondNumber)
print(f"The remainder of dividing {firstNumber} by {secondNumber} is: {remainder}")